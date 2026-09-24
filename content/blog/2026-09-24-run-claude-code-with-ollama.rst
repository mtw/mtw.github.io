Run Claude Code with Ollama on macOS and Linux
##############################################

:date: 2026-09-24
:tags: AI; tools
:category: howto
:section: guides
:slug: claude-code-ollama-local-llm
:title: Run Claude Code with Ollama: a local LLM on macOS and Linux
:summary: Ollama serves Anthropic's Messages API since version 0.14, so Claude Code connects to it directly. Setup on macOS and Linux, the context-length trap, model choice, and what does not work.
:description: How to connect Claude Code to Ollama's Anthropic-compatible endpoint on macOS or Linux, set the context length, and pick a model with tool calling.

.. role:: link-flat(link)
  :class: m-flat m-text

Since Ollama 0.14.0 (January 2026) the Ollama server answers Anthropic's Messages API
on ``http://localhost:11434/v1/messages``. Claude Code therefore works against it with
two environment variables, on a Mac or on a Linux box with an NVIDIA or AMD GPU. The
setup is shorter than the :link-flat:`LM Studio variant <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>`;
the one thing that regularly goes wrong is the context length, which Ollama picks
from your GPU memory and which is far too small by default on most machines.

Prerequisites
-------------

- `Ollama <https://ollama.com/>`_ 0.14.0 or newer (``ollama --version``).
- Claude Code (``curl -fsSL https://claude.ai/install.sh | bash``).
- Memory: about 19 GB free for ``qwen3-coder`` (30B mixture-of-experts, 3B active),
  16 GB for ``gpt-oss:20b``; on Linux that means GPU memory for full speed, otherwise
  Ollama falls back to the CPU and everything becomes slow.

Step 1: Pull a model that can call tools
----------------------------------------

.. code-block:: bash

   ollama pull qwen3-coder      # 19 GB, 256K native context, the better coder
   ollama pull gpt-oss:20b      # 14 GB, 128K context, Ollama's own suggestion

Claude Code drives the model through tool calls (read file, edit file, run command).
Both models above support that; many small chat models do not, and with those the
agent talks but never acts.

Step 2: Set the context length
------------------------------

Ollama chooses a default context from available GPU memory: 4K below 24 GiB, 32K
between 24 and 48 GiB, 256K above. Claude Code's system prompt and tool definitions
alone are about 20K tokens, so on a laptop the 4K default fails on the first request
with a context-limit error. Start the server with an explicit value:

.. code-block:: bash

   OLLAMA_CONTEXT_LENGTH=32768 ollama serve

On macOS with the Ollama app, set the context in the app's settings instead (the app
runs the server for you), or quit the app and run ``ollama serve`` from a terminal as
above. On Linux with the systemd service, add the variable to the service:

.. code-block:: bash

   sudo systemctl edit ollama
   # in the editor, add:
   # [Service]
   # Environment="OLLAMA_CONTEXT_LENGTH=32768"
   sudo systemctl restart ollama

Verify with ``ollama ps``: the ``CONTEXT`` column must show 32768 (or more) once a
model is loaded. Larger contexts cost memory; 64K is a good target if it fits.

Step 3: Point Claude Code at Ollama
-----------------------------------

.. code-block:: bash

   export ANTHROPIC_BASE_URL=http://localhost:11434
   export ANTHROPIC_AUTH_TOKEN=ollama          # required by Claude Code, ignored by Ollama
   export ANTHROPIC_DEFAULT_HAIKU_MODEL=qwen3-coder
   export ANTHROPIC_DEFAULT_SONNET_MODEL=qwen3-coder
   export ANTHROPIC_DEFAULT_OPUS_MODEL=qwen3-coder
   claude --model qwen3-coder

The alias mapping matters: Claude Code uses its ``haiku`` alias for background work,
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

Sources: `Ollama, Anthropic compatibility <https://docs.ollama.com/api/anthropic-compatibility>`_;
`Ollama blog, Claude Code with Anthropic API compatibility (16 January 2026) <https://ollama.com/blog/claude>`_;
`Ollama, context length <https://docs.ollama.com/context-length>`_;
`Claude Code, model configuration <https://code.claude.com/docs/en/model-config>`_.
