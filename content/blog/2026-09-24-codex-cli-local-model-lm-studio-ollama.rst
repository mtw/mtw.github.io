Run OpenAI Codex CLI with a local model (LM Studio or Ollama)
#############################################################

:date: 2026-09-24
:modified: 2026-10-28
:tags: AI; tools
:category: howto
:section: guides
:bridge: tools
:slug: codex-cli-local-model-lm-studio-ollama
:feedback: guide
:title: Codex CLI with a local model: LM Studio and Ollama setup, models, troubleshooting
:summary: Codex CLI has a built-in local mode. This guide covers the flag and the config profile, which local models work for agentic coding and what they need, Ollama's one-command launcher, Linux GPU notes, and the errors you will meet.
:description: How to run OpenAI's Codex CLI with a local model: --oss with LM Studio or Ollama, config.toml profiles, which models work, context length, common errors.

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: series-note

   Local AI coding tools, a short series: :link-flat:`Claude Code with LM Studio <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>` · :link-flat:`Claude Code with Ollama <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>` · Codex CLI with a local model (this post) · :link-flat:`Claude Code for data analysis with a local model <{filename}/blog/2026-10-28-claude-code-csv-reproducible-analysis.rst>`

Codex, OpenAI's terminal coding agent, can use a local model, the mode is built in: ``codex --oss`` sends
its requests to a model server on your machine instead of OpenAI's API. LM Studio and
Ollama both support it, so the setup is a few commands. This guide was written in
September 2026 and expanded in October 2026 after it became the page people reach for
"codex local model"; it now covers the model choice, Ollama's launcher, a persistent
configuration, Linux machines, and the failures I have seen; the commands were re-run
with Codex 0.163, LM Studio 0.4.16 and Ollama 0.40. Codex differs from Claude Code in
two ways that matter locally: it speaks OpenAI's *Responses* API only, and it uses more
context.

Prerequisites
-------------

- Codex CLI: ``npm install -g @openai/codex`` (``codex --version`` to confirm).
- A current LM Studio (0.3.29 added the Responses endpoint) or a current Ollama.
- A model with tool calling and a large context window; see the next section for
  memory. Codex also wants a project directory to work in; it reads an ``AGENTS.md``
  there if present, which is the right place for durable instructions.

Choosing a local model
----------------------

Codex drives the model through tool calls (read, edit, run) and sends a long system
prompt, so two properties decide whether a model is usable: reliable tool calling and a
context of at least 64K tokens (Ollama's recommendation for Codex; LM Studio says "more
than ~25k", which is the floor rather than a comfortable value). The models below have
both; the memory figures are what the server needs with a 64K context loaded.

``openai/gpt-oss-20b`` (Ollama: ``gpt-oss:20b``)
   14 GB download, about 16 GB of memory, 128K context, tool calling and reasoning
   built in. The default for ``codex --oss`` and the sensible first choice on a 24–32 GB
   Mac or a 24 GB GPU.

``qwen/qwen3-coder-30b`` (Ollama: ``qwen3-coder``)
   19 GB, a 30B mixture-of-experts model with 3B active parameters, 256K context. In my
   use the stronger coder of the two for edits across several files; needs 32 GB or more.

``openai/gpt-oss-120b`` (Ollama: ``gpt-oss:120b``)
   65 GB, meant for an 80 GB GPU or a 96–128 GB Mac. Noticeably better judgement on
   larger tasks; out of reach on ordinary hardware.

``google/gemma-4-12b`` (Ollama: ``gemma4``)
   About 7 GB on disk, 12 GB loaded with a 32K context. The option for a 16 GB machine;
   it completed file-editing tasks in my tests. Smaller models (``ibm/granite-4-micro``
   and similar) run too, but tend to narrate edits instead of making them; see the
   troubleshooting section.

Measured on a 24 GB Mac with a 32K context: ``gpt-oss:20b`` loads fully on the GPU;
``qwen3-coder`` fits only partly (16 of 19 GB) and slows down; a dense 27B model such as
``qwen3.8`` runs out of GPU memory under Codex's prompt. 24 GB means gpt-oss-20b.

With LM Studio
--------------

.. code-block:: bash

   lms load openai/gpt-oss-20b --context-length 65536
   lms server start --port 1234
   codex --oss --local-provider lmstudio
   codex --oss --local-provider lmstudio -m qwen/qwen3-coder-30b   # any other loaded model

Codex talks to ``http://localhost:1234/v1/responses``. Load the model yourself with
``--context-length`` as above: if Codex's first request triggers the load (LM Studio
does load on demand, and a short task then succeeds), the model gets the server's
default context, which is usually far too small, and the session fails with a context
error a few turns in. ``lms ps`` shows what is loaded and with which context. Download
models through LM Studio's catalog (``lms get openai/gpt-oss-20b``): a GGUF from an
arbitrary repository can carry a chat template that fails on Codex's tool definitions
("Error rendering prompt with jinja template").

With Ollama
-----------

.. code-block:: bash

   OLLAMA_CONTEXT_LENGTH=65536 ollama serve     # one terminal (or the app's settings)
   ollama pull gpt-oss:20b
   codex --oss --local-provider ollama -m gpt-oss:20b   # another terminal

Ollama's default context depends on GPU memory and is 4K on most laptops, which is not
enough for Codex; the context-length section of the
:link-flat:`Ollama guide for Claude Code <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>`
explains the setting for the app, the terminal and the Linux service. ``ollama ps`` must
show 65536 in the CONTEXT column.

Two things to know about the built-in ``ollama`` provider. It always talks to
``localhost:11434`` and ignores ``OLLAMA_HOST``; for a model server on another machine,
define your own provider (below). And if the model is not present, Codex pulls it
without asking — ``codex --oss`` on a machine with an empty Ollama starts a 13 GB
download of ``gpt-oss:20b``.

``ollama launch codex``
=======================

Ollama ships a launcher that does the configuration for you:

.. code-block:: bash

   ollama launch codex                 # picks a model, writes a profile, starts Codex
   codex --profile ollama-launch       # reuse that profile later

The launcher writes ``~/.codex/ollama-launch.config.toml`` — a provider
``ollama-launch`` (``base_url = "http://localhost:11434/v1/"``, ``wire_api =
"responses"``), the chosen model and a ``model_catalog_json`` listing your local models
so that ``/model`` inside Codex can switch between them — and starts Codex with that
profile. ``ollama launch codex --config`` writes the profile without starting,
``--restore`` removes it again. Two details: if you sign in with ``ollama signin`` the
profile can use Ollama's web search from inside Codex, and
``codex --profile ollama-launch -c 'web_search="disabled"'`` turns that off for a fully
local session. The launcher does not set the context length; that still comes from
``OLLAMA_CONTEXT_LENGTH`` or the app.

Make it permanent with a profile
--------------------------------

Instead of flags, put the choice in ``~/.codex/config.toml``. The simplest form sets the
local provider for ``--oss``:

.. code-block:: toml

   oss_provider = "lmstudio"        # or "ollama"
   model = "openai/gpt-oss-20b"
   model_context_window = 65536     # what you loaded; lets Codex compact in time

With that, ``codex --oss`` needs no further flags (without it, the interactive CLI asks
which provider to use, and ``codex exec`` exits with an error). The provider IDs
``lmstudio``, ``ollama`` and ``openai`` are built in and cannot be redefined. A custom
provider is needed only for a server that is not on ``localhost`` — a GPU box in the
next room, say:

.. code-block:: toml

   [model_providers.ollama-gpu]
   name = "Ollama on the GPU box"
   base_url = "http://gpubox.local:11434/v1"
   wire_api = "responses"

   [profiles.gpu]
   model_provider = "ollama-gpu"
   model = "gpt-oss:20b"
   model_context_window = 65536

Then ``codex --profile gpu``. ``wire_api = "responses"`` is the default and the only value
Codex accepts: a server that implements only Chat Completions (older llama.cpp, vLLM or
``mlx_lm`` setups) answers Codex's requests with 404 and cannot be used directly; current
LM Studio and Ollama serve ``/v1/responses``. Model names must be the server's API
identifiers (``ollama ls``, or LM Studio's Developer tab), not display names. Command-line
flags override the file for a single run.

On Linux
--------

Everything above works unchanged on Linux. What differs is where the model runs:

- **Ollama** uses NVIDIA (CUDA) and AMD (ROCm) GPUs and falls back to the CPU when the
  model does not fit; ``ollama ps`` shows the split (``100% GPU`` is what you want). A
  20B model with a 64K context needs a 24 GB card; 16 GB cards run it partly on the CPU
  and become slow. The service reads ``OLLAMA_CONTEXT_LENGTH`` from ``systemctl edit
  ollama``, not from your shell.
- **LM Studio** has a Linux build with CUDA and Vulkan backends; the same ``lms`` commands
  apply. LM Studio's *LM Link* can also run the model on a remote machine while Codex
  runs on your laptop, which is the practical answer when the GPU box is elsewhere.

Troubleshooting
---------------

``404`` on every request
   The server does not implement ``/v1/responses`` (Chat Completions only, or an old
   version). Update LM Studio or Ollama, or point the profile at a server that does.

A download starts that you did not ask for
   The built-in Ollama provider pulls a model that is not present locally. Stop it
   with Ctrl-C, ``ollama pull`` the model you want, and name it with ``-m``.

``stream disconnected before completion: Error rendering prompt with jinja template``
   The model file's chat template fails on Codex's tool definitions (LM Studio). Use
   the catalog build of the model (``lms get …``) or override the template in LM Studio's
   model settings; nothing on the Codex side is wrong.

``stream disconnected … Insufficient Memory`` (Metal) or a CUDA out-of-memory error
   The model plus KV cache does not fit the GPU. Smaller model or shorter context; on
   24 GB that means ``gpt-oss:20b``.

The model is reported as missing
   The name is a display label, not the API identifier. Copy it from ``ollama ls`` or
   LM Studio's Developer view (``qwen/qwen3-coder-30b``, not "Qwen3 Coder 30B").

A context or token-limit error after a few turns
   The server runs with its default context. Load the model with
   ``--context-length 65536`` (LM Studio) or start Ollama with
   ``OLLAMA_CONTEXT_LENGTH=65536``; verify with ``lms ps`` / ``ollama ps``.

Codex says it edited a file but nothing changed, or prints tool calls as text
   The model's tool calling is unreliable. Use ``gpt-oss:20b`` or ``qwen3-coder``; keep
   tasks to one to three files; ask for the change, then ask for the test run, rather
   than both in one prompt.

Codex forgets a constraint you gave three turns ago
   Local models hold instructions less firmly than the hosted ones. Put durable rules
   in ``AGENTS.md`` in the project, and restate the critical constraint at the end of a
   long prompt.

Slow on Linux
   The model spilled to the CPU. Smaller quantisation, smaller model, or a shorter
   context; ``ollama ps`` tells you which.

``Connection refused``
   No server on the port in the profile. ``lms server status`` or ``ollama ps``; check
   that the base URL in the profile matches.

What to expect
--------------

The 20B models handle scoped work — a new function with tests, a refactor within a file,
a script, documentation — and lose the thread in large multi-file changes. Give Codex a
small, verifiable task, let it run the tests, and read the diff. Compared with Claude Code
on the same local model, Codex is more demanding on context and a little more fragile with
weak tool callers; with ``gpt-oss:20b`` and 64K of context both work well for the kind of
scripting a research group does every day.

Sources: `LM Studio, Codex integration <https://lmstudio.ai/docs/integrations/codex>`_;
`Ollama, Codex CLI integration <https://docs.ollama.com/integrations/codex>`_;
`Codex configuration reference <https://developers.openai.com/codex/config-reference>`_;
`Ollama library, gpt-oss <https://ollama.com/library/gpt-oss>`_ and
`qwen3-coder <https://ollama.com/library/qwen3-coder>`_;
`Codex CLI local mode with Ollama or LM Studio (ynaito.dev) <https://ynaito.dev/en/writing/codex-cli-local-models-oss/>`_.
