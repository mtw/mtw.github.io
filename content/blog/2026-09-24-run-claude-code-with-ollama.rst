Run Claude Code with Ollama on macOS, Linux and Windows
#######################################################

:date: 2026-09-24
:modified: 2026-10-28
:tags: AI; tools
:category: howto
:section: guides
:bridge: tools
:slug: claude-code-ollama-local-llm
:title: Run Claude Code with Ollama: ollama launch claude, manual setup, context length, models
:summary: Ollama serves Anthropic's Messages API since version 0.14, so Claude Code connects to it directly. The one-command launcher, the manual setup on macOS and Linux, the context-length trap, measured memory needs, a model on another machine, and what does not work.
:description: Claude Code with Ollama on macOS or Linux: ollama launch claude or manual setup, context length, which models fit 16/24/32 GB, remote servers, common errors.

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: series-note

   Local AI coding tools, a short series: :link-flat:`Claude Code with LM Studio <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>` · Claude Code with Ollama (this post) · :link-flat:`Codex CLI with a local model <{filename}/blog/2026-09-24-codex-cli-local-model-lm-studio-ollama.rst>` · :link-flat:`Claude Code for data analysis with a local model <{filename}/blog/2026-10-28-claude-code-csv-reproducible-analysis.rst>`

Claude Code runs against Ollama with two environment variables, because since Ollama
0.14.0 (January 2026) the Ollama server answers Anthropic's Messages API on
``http://localhost:11434/v1/messages``: on a Mac, on a Linux box with an NVIDIA or AMD
GPU, or on Windows. The setup is shorter than the :link-flat:`LM Studio variant <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>`;
the one thing that regularly goes wrong is the context length, which Ollama picks
from your GPU memory and which is far too small by default on most machines. Revised in
October 2026: all commands re-run with Ollama 0.40 and Claude Code 2.1.302, on a 24 GB
M4 Pro acting as the model server.

Prerequisites
-------------

- `Ollama <https://ollama.com/>`_ 0.14.0 or newer (``ollama --version``).
- Claude Code (``curl -fsSL https://claude.ai/install.sh | bash``).
- Memory: measured with a 32K context, ``gpt-oss:20b`` occupies 12 GB and
  ``qwen3-coder`` 19 GB (see the model section); on Linux that means GPU memory for full
  speed, otherwise Ollama falls back to the CPU and everything becomes slow.

The short way: ``ollama launch claude``
---------------------------------------

Recent Ollama releases include a launcher that configures Claude Code for you:

.. code-block:: bash

   ollama launch claude                       # pick a model from the menu, Claude Code starts
   ollama launch claude --model gpt-oss:20b --yes      # non-interactive, pulls the model if needed
   ollama launch claude --model gpt-oss:20b --yes -- -p "how does this repository work?"
   ollama launch claude --config              # configure without starting
   ollama launch claude --restore             # back to the defaults

The launcher sets the environment variables described below for that session, so you
do not have to. It does not set the context length — that is a server setting, and the
next sections explain it — and it hides what happens, which is why the manual way is
worth knowing.

Step 1: Pull a model that can call tools
----------------------------------------

.. code-block:: bash

   ollama pull gpt-oss:20b      # 14 GB download, 12 GB loaded with 32K context; 128K native
   ollama pull qwen3-coder      # 19 GB loaded, 256K native; the better coder, wants 32 GB
   ollama pull qwen3.8          # 18 GB download, dense 27B; strong, needs 32 GB or more

Claude Code drives the model through tool calls (read file, edit file, run command).
All three support that (``ollama show <model>`` lists ``tools`` under *Capabilities*);
many small chat models do not, and with those the agent talks but never acts. What
fits where, measured on a 24 GB Mac with a 32K context: ``gpt-oss:20b`` loads
entirely on the GPU and completes edit tasks; ``qwen3-coder`` loads with 16 of its
19 GB on the GPU and the rest on the CPU, works, but slower; ``qwen3.8:27b`` runs out
of GPU memory as soon as Claude Code's 20K-token prompt arrives. On 16 GB, use
``gemma4`` (the 12B at about 8 GB) or ``qwen3.5:9b`` with a 16K context.

Step 2: Set the context length
------------------------------

Ollama chooses a default context from available GPU memory: 4K below 24 GiB, 32K
between 24 and 48 GiB, 256K above. Claude Code's system prompt and tool definitions
alone are about 20K tokens, so on a laptop the 4K default fails on the first request
with a context-limit error. Start the server with an explicit value:

.. code-block:: bash

   OLLAMA_CONTEXT_LENGTH=32768 ollama serve

On macOS with the Ollama app, move the context-length slider in the app's settings
instead (the app runs the server for you), or quit the app and run ``ollama serve`` from
a terminal as above. On Linux with the systemd service, add the variable to the service:

.. code-block:: bash

   sudo systemctl edit ollama
   # in the editor, add:
   # [Service]
   # Environment="OLLAMA_CONTEXT_LENGTH=32768"
   sudo systemctl restart ollama

On Windows, Ollama runs from the system tray and reads the variable from your account's
environment: quit Ollama, open *Edit environment variables for your account* (search
for "environment variables" in Settings), add ``OLLAMA_CONTEXT_LENGTH`` with the value
``32768``, and start Ollama again from the Start menu. I have not run the Windows setup
myself; this follows Ollama's documentation.

Verify with ``ollama ps``: the ``CONTEXT`` column must show 32768 (or more) once a
model is loaded. Ollama's own recommendation for coding agents is 64K; use it when the
memory allows, 32K is the floor at which Claude Code works.

Step 3: Point Claude Code at Ollama
-----------------------------------

.. code-block:: bash

   export ANTHROPIC_BASE_URL=http://localhost:11434
   export ANTHROPIC_AUTH_TOKEN=ollama          # required by Claude Code, ignored by Ollama
   export ANTHROPIC_DEFAULT_HAIKU_MODEL=qwen3-coder
   export ANTHROPIC_DEFAULT_SONNET_MODEL=qwen3-coder
   export ANTHROPIC_DEFAULT_OPUS_MODEL=qwen3-coder
   export CLAUDE_CODE_MAX_CONTEXT_TOKENS=32768    # the context you set on the server
   claude --model qwen3-coder

In PowerShell the same lines read ``$env:ANTHROPIC_BASE_URL = "http://localhost:11434"``
and so on; or put them in ``.claude/settings.json`` as shown below, which is identical on
every platform.

``CLAUDE_CODE_MAX_CONTEXT_TOKENS`` matters since Claude Code 2.1.193: for a model name it
does not know it assumes a 200K window (and says so with a
``[claude-code:unrecognized_model]`` line); with the real value it compacts the
conversation before Ollama rejects it. Ollama's documentation also sets
``ANTHROPIC_API_KEY=""`` so that no stale key competes with the token. The alias mapping matters: Claude Code uses its ``haiku`` alias for background work,
and without the mapping that call asks Ollama for an Anthropic model name it does not
have. (Ollama's documentation offers ``ollama cp qwen3-coder claude-3-5-sonnet`` as an
alternative — copying the model under an Anthropic name — but the environment
variables are cleaner.) The same variables can live in ``.claude/settings.json`` under
``"env"`` for a per-project setup; see the LM Studio guide for the JSON.

``/status`` inside Claude Code confirms the base URL in use. Add ``DISABLE_TELEMETRY=1``,
``DISABLE_ERROR_REPORTING=1`` and ``CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`` if the
session should not talk to anything but Ollama.

Step 4: Check the endpoint directly if something fails
------------------------------------------------------

.. code-block:: bash

   curl http://localhost:11434/v1/messages \
     -H "content-type: application/json" -H "x-api-key: ollama" \
     -d '{"model":"qwen3-coder","max_tokens":64,
          "messages":[{"role":"user","content":"Say hello in one line."}]}'

The model on another machine
----------------------------

A laptop with 16 GB and a desktop with a GPU is a common pair. Ollama on the desktop
listens on all interfaces when started with ``OLLAMA_HOST=0.0.0.0 ollama serve`` (or the
same variable in the systemd service); on the laptop, point Claude Code at it:

.. code-block:: bash

   export ANTHROPIC_BASE_URL=http://desktop.local:11434     # or a Tailscale/VPN name
   export ANTHROPIC_AUTH_TOKEN=ollama
   export OLLAMA_HOST=http://desktop.local:11434            # so that `ollama ps` etc. also go there

The rest is identical; I run this setup over Tailscale and the only difference is the
hostname. Keep such a server off the open internet: Ollama has no authentication of
its own.

What Ollama's endpoint supports — and what it does not
------------------------------------------------------

Supported: streaming, system prompts, multi-turn conversations, tool calling,
extended thinking, base64 images. Not supported: forced ``tool_choice``, prompt
caching, the token-counting endpoint, URL images, PDFs, batches. In practice the
missing token counter means Claude Code's context indicator can be off, and the missing
prompt cache means every turn re-processes the full prompt — the main reason local
sessions feel slower than the API even on fast hardware.

Troubleshooting
---------------

``400`` with a context or token limit in the message
   The server runs with the default 4K context. Set ``OLLAMA_CONTEXT_LENGTH`` as
   above and confirm with ``ollama ps``.

No answer at all, or "stream disconnected" in the server log
   The model plus its KV cache does not fit the GPU memory; the Metal or CUDA runner
   aborts (``Insufficient Memory`` in ``ollama serve``'s output) and Claude Code shows
   nothing or exits. A dense 27B model with a 32K context does this on 24 GB. Use a
   smaller model or a shorter context.

"claude.ai connectors are disabled because ANTHROPIC_API_KEY or another auth source is set"
   Expected with ``ANTHROPIC_AUTH_TOKEN`` set; the claude.ai-bound features are off for
   the session. Harmless.

``404`` model not found, often mid-session
   The ``haiku`` alias is unmapped. Set ``ANTHROPIC_DEFAULT_HAIKU_MODEL``.

``Connection refused``
   ``ollama serve`` is not running, or the app runs on a different port.

Answers arrive but no file changes
   The model does not support tool calling; use ``qwen3-coder`` or ``gpt-oss:20b``.

Very slow on Linux
   The model does not fit in GPU memory and runs partly on the CPU; ``ollama ps``
   shows the CPU/GPU split. Use a smaller model or quantisation.

Related: :link-flat:`Claude Code with LM Studio on Apple Silicon <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>`
and :link-flat:`OpenAI Codex CLI with a local model <{filename}/blog/2026-09-24-codex-cli-local-model-lm-studio-ollama.rst>`.

Sources: `Ollama, Claude Code integration <https://docs.ollama.com/integrations/claude-code>`_;
`Ollama, Anthropic compatibility <https://docs.ollama.com/api/anthropic-compatibility>`_;
`Ollama blog, Claude Code with Anthropic API compatibility (16 January 2026) <https://ollama.com/blog/claude>`_;
`Ollama, context length <https://docs.ollama.com/context-length>`_;
`Claude Code, model configuration <https://code.claude.com/docs/en/model-config>`_.
