Run OpenAI Codex CLI with a local model (LM Studio, Ollama or exo)
##################################################################

:date: 2026-09-24
:modified: 2026-11-11
:tags: AI; tools
:category: howto
:section: guides
:bridge: tools
:slug: codex-cli-local-model-lm-studio-ollama
:feedback: guide
:title: Codex CLI with a local model: LM Studio, Ollama and exo setup, models, troubleshooting
:summary: Codex CLI has a built-in local mode. This guide covers the flag and the config profile, which local models work for agentic coding and what they need, Ollama's one-command launcher, exo for pooling several machines into one server, Linux GPU notes, and the errors you will meet.
:description: Run OpenAI's Codex CLI on a local model: --oss with LM Studio or Ollama, an exo cluster, config profiles, which models work, context, common errors.

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: series-note

   Local AI coding tools, a short series: :link-flat:`Claude Code with LM Studio <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>` · :link-flat:`Claude Code with Ollama <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>` · Codex CLI with a local model (this post) · :link-flat:`Claude Code for data analysis with a local model <{filename}/blog/2026-10-28-claude-code-csv-reproducible-analysis.rst>` · :link-flat:`four agents against ten models <{filename}/blog/2026-11-14-coding-agents-local-models-exo-cluster.rst>`

Codex, OpenAI's terminal coding agent, can use a local model, the mode is built in: ``codex --oss`` sends
its requests to a model server on your machine instead of OpenAI's API. LM Studio and
Ollama both support it, so the setup is a few commands, and exo serves the same API
across several machines at once. This guide was written in
September 2026 and expanded in October 2026 after it became the page people reach for
"codex local model". It now covers the model choice, Ollama's launcher, a persistent
configuration, Linux machines and the failures I have seen, and the commands were re-run
with Codex 0.163, LM Studio 0.4.16 and Ollama 0.40. Codex differs from Claude Code in
two ways that matter locally. It speaks OpenAI's *Responses* API only. It uses more
context.

.. frame:: Workshop in preparation

   These setup notes are what a half-day workshop for research groups is built on, for
   groups whose unpublished data and code must not leave their own machines. It has no
   date yet. The `waiting list at RNA Forecast <https://rnaforecast.com/training/?utm_source=michaelwolfinger&utm_medium=referral&utm_campaign=local-ai-tools&utm_content=codex-cli#local-ai-tools>`_
   sends one e-mail when a first date exists, and nothing else.

Prerequisites
-------------

- Codex CLI: ``npm install -g @openai/codex`` (``codex --version`` to confirm).
- A current LM Studio (0.3.29 added the Responses endpoint) or a current Ollama.
- A model with tool calling and a large context window; see the next section for
  memory. Codex also wants a project directory to work in. It reads an ``AGENTS.md``
  there if present, which is the right place for durable instructions.

Choosing a local model
----------------------

Codex drives the model through tool calls (read, edit, run) and sends a long system
prompt, so two properties decide whether a model is usable: reliable tool calling and a
context of at least 64K tokens (Ollama's recommendation for Codex, while LM Studio says
"more than ~25k", which is the floor rather than a comfortable value). The models below
have both, and the memory figures are what the server needs with a 64K context loaded.

``openai/gpt-oss-20b`` (Ollama: ``gpt-oss:20b``)
   14 GB download, about 16 GB of memory, 128K context, tool calling and reasoning
   built in. The default for ``codex --oss`` and the sensible first choice on a 24–32 GB
   Mac or a 24 GB GPU.

``qwen/qwen3-coder-30b`` (Ollama: ``qwen3-coder``)
   19 GB, a 30B mixture-of-experts model with 3B active parameters, 256K context. In my
   use the stronger coder of the two for edits across several files. Wants 32 GB or more.

``openai/gpt-oss-120b`` (Ollama: ``gpt-oss:120b``)
   65 GB, meant for an 80 GB GPU or a 96–128 GB Mac. Noticeably better judgement on
   larger tasks, but out of reach on ordinary hardware.

``google/gemma-4-12b`` (Ollama: ``gemma4``)
   About 7 GB on disk, 12 GB loaded with a 32K context. It completed file-editing
   tasks in my tests. This is the one that works on a smaller machine, though on 16 GB it
   is a Claude Code answer rather than a Codex one: see the measurements above for why.
   Smaller models (``ibm/granite-4-micro`` and similar) run too, but tend to narrate edits
   instead of making them, as the troubleshooting section describes.

Measured on a 24 GB Mac with a 32K context: ``gpt-oss:20b`` loads fully on the GPU, while
``qwen3-coder`` fits only partly (16 of 19 GB) and slows down, and a dense 27B model such
as ``qwen3.8`` runs out of GPU memory under Codex's prompt. On 24 GB that leaves
gpt-oss-20b as the working choice. That ceiling is a property of the single machine
rather than of Codex, and pooling several machines with exo is the way past it.

With LM Studio
--------------

.. code-block:: bash

   lms load openai/gpt-oss-20b --context-length 65536
   lms server start --port 1234
   codex --oss --local-provider lmstudio
   codex --oss --local-provider lmstudio -m qwen/qwen3-coder-30b   # any other loaded model

Codex talks to LM Studio on the URL ``http://localhost:1234/v1/responses``. Load the model yourself with
``--context-length`` as above: if Codex's first request triggers the load (LM Studio
does load on demand, and a short task then succeeds), the model gets the server's
default context, which is usually far too small, and the session fails with a context
error a few turns in. ``lms ps`` shows what is loaded and with which context. Download
models through LM Studio's catalog (``lms get openai/gpt-oss-20b``): a GGUF from an
arbitrary repository can carry a chat template that fails on Codex's tool definitions
("Error rendering prompt with jinja template").

On a 16 GB Mac this does not work. The numbers are worth having, because 16 GB is the
entry configuration of every Apple laptop and the one a reader is most likely to be told
is enough. LM Studio refuses a load it expects to exhaust the machine. On an M1 Pro with
16 GB it reports:

.. code-block:: text

   openai/gpt-oss-20b       64K   refused
   openai/gpt-oss-20b       32K   refused
   google/gemma-4-12b-qat   64K   refused, needs about 17.2 GB
   google/gemma-4-12b-qat   32K   refused, needs about 12.2 GB
   google/gemma-4-12b-qat   24K   refused, needs about 11.0 GB
   google/gemma-4-12b-qat   16K   loads, 7.15 GB

The limit is the model plus the KV cache for the context you ask for, so the context is
what pushes it over. 16K is the largest that loads here, which is below the floor Codex
needs, so a 16 GB machine is short of what this costs. Three ways out: raise the guardrail
in LM Studio's settings and accept that the machine swaps when anything else wants memory;
use Ollama, which has no such guardrail and spills to swap instead of refusing; or add a
second machine with exo, below. Claude Code is the other option on this hardware, since it
asks for less context than Codex does.

With Ollama
-----------

.. code-block:: bash

   OLLAMA_CONTEXT_LENGTH=65536 ollama serve     # one terminal (or the app's settings)
   ollama pull gpt-oss:20b
   codex --oss --local-provider ollama -m gpt-oss:20b   # another terminal

Ollama's default context depends on GPU memory and is 4K on most laptops, which is not
enough for Codex, and the context-length section of the
:link-flat:`Ollama guide for Claude Code <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>`
explains the setting for the app, the terminal and the Linux service. ``ollama ps`` must
show 65536 in the CONTEXT column.

Two things to know about the built-in ``ollama`` provider. It always talks to
``localhost:11434`` and ignores ``OLLAMA_HOST``, so for a model server on another machine,
define your own provider (below). If the model is not present, Codex pulls it without asking—``codex --oss`` on a machine with an empty Ollama starts a 13 GB
download of ``gpt-oss:20b``.

``ollama launch codex``
=======================

Ollama ships a launcher that does the configuration for you:

.. code-block:: bash

   ollama launch codex                 # picks a model, writes a profile, starts Codex
   codex --profile ollama-launch       # reuse that profile later

The launcher writes ``~/.codex/ollama-launch.config.toml``—a provider
``ollama-launch`` (``base_url = "http://localhost:11434/v1/"``, ``wire_api =
"responses"``), the chosen model and a ``model_catalog_json`` listing your local models
so that ``/model`` inside Codex can switch between them—and starts Codex with that
profile. ``ollama launch codex --config`` writes the profile without starting,
``--restore`` removes it again. Two details: if you sign in with ``ollama signin`` the
profile can use Ollama's web search from inside Codex, and
``codex --profile ollama-launch -c 'web_search="disabled"'`` turns that off for a fully
local session. The launcher does not set the context length, which still comes from
``OLLAMA_CONTEXT_LENGTH`` or the app.

With exo
--------

`exo <https://github.com/exo-explore/exo>`_ pools several machines into one model server,
which is the way around the memory ceiling above: a model too large for any single Mac runs
across two or three of them. It answers ``POST /v1/responses`` on port 52415, so Codex
drives it like any other provider. The setup behind the numbers below is two 24 GB Macs
running ``mlx-community/gemma-4-31b-it-4bit`` split across both. The 6-bit loads as well,
and the reason not to use it with an agent is below.

.. code-block:: bash

   brew install --cask exo        # Apple silicon, macOS 15.1 or later
   exo                            # or `uv run exo` from a source checkout

Port 52415 is not one of the built-in provider IDs, so it needs a provider block in
``~/.codex/config.toml``:

.. code-block:: toml

   [model_providers.exo]
   name = "exo cluster"
   base_url = "http://localhost:52415/v1"
   wire_api = "responses"

and the profile that selects it in its own file, ``~/.codex/exo.config.toml``:

.. code-block:: toml

   model_provider = "exo"
   model = "mlx-community/gemma-4-31b-it-4bit"   # an id from GET /models
   model_context_window = 65536

Then ``codex --profile exo``. A ``[profiles.exo]`` table inside ``config.toml`` is the
older form. Codex 0.167 refuses ``--profile`` while one is present and names the file
above as the replacement. ``base_url`` stays on ``localhost`` when Codex runs on one of
the cluster's own machines. From a laptop it is that node's address and port 52415 instead.

exo's own integrations page writes the provider with ``env_key = "EXO_API_KEY"`` and
launches Codex as ``EXO_API_KEY=x npx @openai/codex``, which is the same thing arranged
differently: ``env_key`` tells Codex that a key is required, and the launch command
supplies one. The value is not checked, hence ``x``. Take the config block without that
command and Codex refuses the provider with *"active model provider auth env var is
missing"*, so either keep the two together or leave ``env_key`` out as above, in which case
Codex reports that no auth is required and proceeds. ``codex doctor`` settles all of this
in one command: it prints the provider, the wire API in use, whether auth is satisfied and
whether the endpoint answers.

The same page suggests adding the MCP filesystem server
(``npx -y @modelcontextprotocol/server-filesystem <your directory>``) alongside the
provider, which gives the model file access through MCP rather than through Codex's own
tools.

The model name has to be the id the cluster reports, and
``curl http://localhost:52415/models?status=downloaded`` lists what is actually on disk
rather than what could be fetched. The dashboard sits on the same port.

What exo adds and what it asks in return:

- Nodes discover each other on the same network when they run **the same build** and the
  same cluster name (``--namespace``, or ``EXO_ZENOH_NAMESPACE``; the default is ``exo``).
  A Mac and a Linux machine do not join the same cluster.
- On macOS the GPU is used. **On Linux exo runs on the CPU**, with GPU support described as
  under development, so an NVIDIA box is still Ollama's job.
- RDMA over Thunderbolt is what makes a cluster fast. It wants macOS Tahoe 26.2 or later,
  Thunderbolt 5, and every device cabled to every other.
- The same server also answers ``/v1/chat/completions``, Claude's ``/v1/messages`` and
  Ollama's ``/ollama/api/chat``, so one cluster can serve Codex and Claude Code together.

Models come from the MLX community repositories, and a model outside the catalogue can be
added with ``POST /models/add``; anything that needs ``trust_remote_code`` has to be
enabled deliberately.

What this looks like in practice, on the two-machine cluster above, is that Codex and
gemma 4 do not get along. The full measurement, ten models against four agents, is in
:link-flat:`its own post <{filename}/blog/2026-11-14-coding-agents-local-models-exo-cluster.rst>`. The short version follows. Four coding agents, the same one-file edit, the same model
(``gemma-4-31b-it-4bit``), the same two machines, repeated on three separate occasions:

.. code-block:: text

   agent         API it speaks           result
   Codex         /v1/responses           failed, both runners went down
   Claude Code   /v1/messages            completed the edit
   OpenCode      /v1/chat/completions    completed the edit
   pi            /v1/chat/completions    completed the edit

Three of the four do the work. Codex does not. Within about thirty seconds of its first
request both runners abort and the instance is gone, every time. The same Codex completes
the same edit on ``Huihui-Qwen3.5-27B``, on ``Huihui-Qwen3.5-9B`` and on
``GLM-4.7-Flash-5bit``, so its requests are not harmful as such. It is Codex together with
this model family. ``gpt-oss-20b`` is the only other model on which Codex took a runner
down, once, with a seven-minute hang on another attempt.

The 6-bit gemma (24.3 GB of weights) fails for a different reason, which is not Codex. A
plain chat completion of about 4,000 tokens kills its runners with no agent involved,
while the 4-bit answers 16,000 tokens without complaint. Every coding agent except pi
carries a system prompt and tool schema above that line, so on two 24 GB machines the
6-bit is a chat model rather than an agent model. Setting ``model_context_window``
smaller does not help in either case: for the 6-bit the first request is already too
large, and for the 4-bit the size is not the problem.

What in Codex's traffic does the damage is not pinned down. I rebuilt its requests by hand
and sent nine variants against both endpoints, with tool definitions, a second turn that
feeds a tool result back, streaming, and an eleven thousand token prompt, and all nine
worked. Codex 0.169 adds a developer item to the Responses ``input`` that carries its
code-mode ``exec`` tool (``codex features list`` shows it as ``code_mode_host``), and exo
rejects that request outright with a 422. Switching that feature off
(``codex -c features.code_mode_host=false``) removes the fast failure on gemma: two of
three sessions then ran to the end instead of dying at thirty seconds. Neither of them
edited the file, both ran ``sed`` with a line break inside the pattern, and the third
session's runners died four minutes in, so the tool definition is part of the cause and
not all of it. What remains needs a logging proxy between Codex and exo.

For chat the cluster is unremarkable and useful. ``gemma-4-31b-it-4bit`` generates at 20
tokens a second, the 6-bit at 13 to 14, and ``Qwen3.5-35B-A3B-4bit`` at 61 to 64 because it
is a mixture of experts with 3B active parameters. First token comes back in about a tenth
of a second in each case.

Two practical notes from the same runs. A model small enough for one machine is placed on
one machine by default: for ``gpt-oss-20b`` exo offers a one-node and a two-node placement
and takes the single node unless told otherwise, so below roughly 20 GB the second machine
only helps if you pick the two-runner placement yourself. And two models in the catalogue
cannot drive an agent at all. ``Meta-Llama-3.1-8B-Instruct`` and
``Qwen2.5-Coder-14B-Instruct`` write the tool call out as text instead of making it, under
all four agents, each of which then reports success over an unchanged file.

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
provider is needed only for a server that is not on ``localhost``—a GPU box in the
next room, say:

.. code-block:: toml

   [model_providers.ollama-gpu]
   name = "Ollama on the GPU box"
   base_url = "http://gpubox.local:11434/v1"
   wire_api = "responses"

with the profile in ``~/.codex/gpu.config.toml``, the same layout the launcher uses for
``ollama-launch`` above:

.. code-block:: toml

   model_provider = "ollama-gpu"
   model = "gpt-oss:20b"
   model_context_window = 65536

Then ``codex --profile gpu``. ``wire_api = "responses"`` is the default and the only value
Codex accepts: a server that implements only Chat Completions (older llama.cpp, vLLM or
``mlx_lm`` setups) answers Codex's requests with 404 and cannot be used directly, while
current LM Studio and Ollama serve ``/v1/responses``. Model names must be the server's API
identifiers (``ollama ls``, or LM Studio's Developer tab), not display names. Command-line
flags override the file for a single run.

On Linux
--------

Everything above works unchanged on Linux, and only the place where the model runs differs:

- **Ollama** uses NVIDIA (CUDA) and AMD (ROCm) GPUs and falls back to the CPU when the
  model does not fit, and ``ollama ps`` shows the split (``100% GPU`` is what you want). A
  20B model with a 64K context needs a 24 GB card, while 16 GB cards run it partly on the
  CPU and become slow. The service reads ``OLLAMA_CONTEXT_LENGTH`` from ``systemctl edit
  ollama``, not from your shell.
- **LM Studio** has a Linux build with CUDA and Vulkan backends, and the same ``lms`` commands
  apply. LM Studio's *LM Link* can also run the model on a remote machine while Codex
  runs on your laptop, which is the practical answer when the GPU box is elsewhere.

Troubleshooting
---------------

``404`` on every request
   The server does not implement ``/v1/responses`` (Chat Completions only, or an old
   version). Update LM Studio or Ollama, or point the profile at a server that does. exo
   serves ``/v1/responses`` and is not the cause of this one.

The exo cluster has fewer machines than it should
   The nodes are running different builds, or a different ``--namespace``. Both have to
   match exactly, and a Linux node never joins a Mac cluster.

exo reports a model Codex cannot select
   Codex needs the API id, which ``GET /models?status=downloaded`` gives, and a model that
   appears in a search but has not been downloaded is not yet selectable.

A download starts that you did not ask for
   The built-in Ollama provider pulls a model that is not present locally. Stop it
   with Ctrl-C, ``ollama pull`` the model you want, and name it with ``-m``.

``stream disconnected before completion: Error rendering prompt with jinja template``
   The model file's chat template fails on Codex's tool definitions (LM Studio). Use
   the catalog build of the model (``lms get …``) or override the template in LM Studio's
   model settings, because nothing on the Codex side is wrong.

``stream disconnected … Insufficient Memory`` (Metal) or a CUDA out-of-memory error
   The model plus KV cache does not fit the GPU. Use a smaller model or a shorter context,
   which on 24 GB means ``gpt-oss:20b``.

The model is reported as missing
   The name is a display label, not the API identifier. Copy it from ``ollama ls`` or
   LM Studio's Developer view (``qwen/qwen3-coder-30b``, not "Qwen3 Coder 30B").

A context or token-limit error after a few turns
   The server runs with its default context. Load the model with
   ``--context-length 65536`` (LM Studio) or start Ollama with
   ``OLLAMA_CONTEXT_LENGTH=65536``, then verify with ``lms ps`` or ``ollama ps``.

Codex says it edited a file but nothing changed, or prints tool calls as text
   The model's tool calling is unreliable. Use ``gpt-oss:20b`` or ``qwen3-coder``, keep
   tasks to one to three files, and ask for the change first and for the test run
   afterwards rather than for both in one prompt.

Codex forgets a constraint you gave three turns ago
   Local models hold instructions less firmly than the hosted ones. Put durable rules
   in ``AGENTS.md`` in the project, and restate the critical constraint at the end of a
   long prompt.

Slow on Linux
   The model spilled to the CPU. Use a smaller quantisation, a smaller model or a shorter
   context, and ``ollama ps`` tells you which of them you need.

``Connection refused``
   No server on the port in the profile. Run ``lms server status`` or ``ollama ps``, then
   check that the base URL in the profile matches.

What to expect
--------------

The 20B models handle scoped work—a new function with tests, a refactor within a file,
a script, documentation—and lose the thread in large multi-file changes. Give Codex a
small, verifiable task, let it run the tests, and read the diff. Compared with Claude Code
on the same local model, Codex is more demanding on context and a little more fragile with
weak tool callers, but with ``gpt-oss:20b`` and 64K of context both work well for the kind of
scripting a research group does every day.

.. frame:: On your own code

   The setup above is the easy half. Whether a local model is good enough for the code
   your group actually works with is a question that can only be answered on that code,
   with the tasks you run and the hardware you have. If that is the question in front of
   you, the `same waiting list <https://rnaforecast.com/training/?utm_source=michaelwolfinger&utm_medium=referral&utm_campaign=local-ai-tools&utm_content=codex-cli-end#local-ai-tools>`_
   takes a note of it, and I will know what to prepare.

Sources: `LM Studio, Codex integration <https://lmstudio.ai/docs/integrations/codex>`_ ·
`Ollama, Codex CLI integration <https://docs.ollama.com/integrations/codex>`_ ·
`Codex configuration reference <https://developers.openai.com/codex/config-reference>`_ ·
`Ollama library, gpt-oss <https://ollama.com/library/gpt-oss>`_ and
`qwen3-coder <https://ollama.com/library/qwen3-coder>`_ ·
`Codex CLI local mode with Ollama or LM Studio (ynaito.dev) <https://ynaito.dev/en/writing/codex-cli-local-models-oss/>`_.
