Connect Claude Code to LM Studio: local LLM setup on Apple Silicon
##################################################################

:date: 2026-04-17
:modified: 2026-10-19
:tags: AI; tools
:category: howto
:section: guides
:slug: claude-code-local-llm-apple-silicon
:title: Connect Claude Code to LM Studio: local LLM setup on Apple Silicon
:summary: Connect Claude Code to LM Studio's Anthropic-compatible endpoint and run a local model on Apple Silicon: setup, model choice, context length, and the errors you will actually meet.
:description: Claude Code + LM Studio setup on Apple Silicon: ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN, which local model and context length to use, common errors.

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: series-note

   Local AI coding tools, a short series: Claude Code with LM Studio (this post) · :link-flat:`Claude Code with Ollama <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>` · :link-flat:`Codex CLI with a local model <{filename}/blog/2026-09-24-codex-cli-local-model-lm-studio-ollama.rst>`

Claude Code connects to LM Studio with two environment variables, ``ANTHROPIC_BASE_URL``
and ``ANTHROPIC_AUTH_TOKEN``, because LM Studio has served Anthropic's Messages API on
``localhost:1234`` since version 0.4.1 (January 2026): no proxy, no provider file, no
translation layer. This guide covers the setup on a Mac with Apple Silicon (with notes
for Windows and Linux), how to choose a model and context length that actually work with
an agent, and the failure modes I ran into. It was first written in April 2026 and revised in September and
October 2026; every command below was re-run in October 2026 with LM Studio 0.4.16 and
Claude Code 2.1.302.

I use this for the same reason many scientists will: unpublished sequence data and
manuscripts should not leave the machine, and a local model costs nothing per token.
The trade-off is capability. A 20–30B local model is a competent assistant for scripts,
refactoring, and documentation; it is not a substitute for the frontier models on large
multi-file tasks.

Prerequisites
-------------

- A Mac with Apple Silicon and enough unified memory for the model you want (see
  "Choosing a model" below; 32 GB is comfortable, 16 GB works with small models and a
  shorter context).
- `LM Studio <https://lmstudio.ai/>`_ 0.4.1 or newer, opened at least once.
- Claude Code: ``curl -fsSL https://claude.ai/install.sh | bash`` or
  ``brew install --cask claude-code``, then ``claude --version``.

Step 1: Load a model in LM Studio
---------------------------------

LM Studio ships a command-line tool, ``lms``. If your shell does not find it, run the
bootstrap step from the LM Studio app (Developer tab) and reopen the terminal.

.. code-block:: bash

   lms get qwen/qwen3-coder-30b   # download from LM Studio's catalog (see note below)
   lms ls                         # models on disk
   lms load --estimate-only qwen/qwen3-coder-30b --context-length 32768
   lms load qwen/qwen3-coder-30b --context-length 32768 --identifier qwen-local
   lms ps                         # what is loaded, with its context length

Two settings matter more than anything else:

**Context length.** Claude Code sends a system prompt and tool definitions of roughly
20K tokens before your first word. LM Studio's own guidance is "more than ~25k"; the
model's default in LM Studio is often 4K, and with that the session fails on the first
request. Use 32K as the floor and 64K if memory allows; the KV cache grows with it.

**Tool calling.** The agent edits files and runs commands through tool calls. A model
without reliable tool use will chat about your code and never touch it. Coding models
with tool support that run well on Apple Silicon:

- ``qwen/qwen3-coder-30b`` (30B mixture-of-experts, 3B active; about 19 GB at 4-bit) —
  the best balance I have found for agentic work; wants 32 GB.
- ``openai/gpt-oss-20b`` (about 12 GB loaded with a 32K context; LM Studio's and
  Ollama's default suggestion) — the choice for 24 GB machines.
- ``qwen/qwen3.8-27b`` (dense 27B, about 18 GB) — the current general model in LM
  Studio's catalog, strong at tool use; needs 32 GB or more once the context is loaded.
- ``google/gemma-4-12b`` (about 7 GB on disk, 12 GB loaded with 32K) — the practical
  option for a 16 GB Mac; it completed file-editing tasks reliably in my tests.

**Where the model comes from matters.** Download through LM Studio's catalog
(``lms get <model>`` or the app's Discover tab), which carries chat templates LM Studio has
tested. A GGUF taken from an arbitrary Hugging Face repository can have a template that
LM Studio's Jinja engine cannot render once an agent sends its tool definitions; the
plain ``curl`` test below then works and Claude Code fails with a 500 (see
troubleshooting).

**Memory on a 16 GB Mac.** The KV cache for a 32K context adds several gigabytes: a 7 GB
model needs about 12 GB loaded, and LM Studio's resource guardrail refuses loads it
expects to freeze the machine. Use ``--context-length 16384`` or a smaller model there,
and close memory-hungry applications.

Step 2: Start the server
------------------------

.. code-block:: bash

   lms server start --port 1234
   lms server status

The Anthropic-compatible endpoint is ``http://localhost:1234/v1/messages``. Check it
before involving Claude Code — first the model list, then one message:

.. code-block:: bash

   curl http://localhost:1234/v1/models      # loaded identifiers, "qwen-local" among them
   curl http://localhost:1234/v1/messages \
     -H "content-type: application/json" \
     -H "x-api-key: lmstudio" \
     -d '{"model":"qwen-local","max_tokens":64,
          "messages":[{"role":"user","content":"Say hello in one line."}]}'

A JSON reply with ``"type":"message"`` means the server side is done.

Step 3: Point Claude Code at LM Studio
--------------------------------------

.. code-block:: bash

   export ANTHROPIC_BASE_URL=http://localhost:1234
   export ANTHROPIC_AUTH_TOKEN=lmstudio
   export ANTHROPIC_DEFAULT_HAIKU_MODEL=qwen-local
   export ANTHROPIC_DEFAULT_SONNET_MODEL=qwen-local
   export ANTHROPIC_DEFAULT_OPUS_MODEL=qwen-local
   export CLAUDE_CODE_MAX_CONTEXT_TOKENS=32768
   claude --model qwen-local

What each line does:

- ``ANTHROPIC_BASE_URL`` sends every request to LM Studio.
- ``ANTHROPIC_AUTH_TOKEN`` is the credential. LM Studio ignores its value unless
  *Require Authentication* is on, in which case use your LM Studio API token. Setting
  it also tells Claude Code not to use your claude.ai login for the session.
- The three ``ANTHROPIC_DEFAULT_*_MODEL`` lines map Claude Code's model aliases to
  the local model. This is the step most guides leave out: Claude Code runs some
  background work on its ``haiku`` alias, and if that alias still resolves to an
  Anthropic model name, LM Studio answers 404 and the session breaks in odd places.
  With the mapping in place, ``/model sonnet`` and friends all mean "the local model".
- ``CLAUDE_CODE_MAX_CONTEXT_TOKENS`` tells Claude Code how large the loaded context
  is. For a model name it does not recognise it assumes 200K tokens and prints
  ``[claude-code:unrecognized_model]`` at startup; with the real value it compacts the
  conversation before LM Studio rejects it. Match the ``--context-length`` you loaded.
- ``--model qwen-local`` selects the model for this session; ``ANTHROPIC_MODEL`` does
  the same from the environment.

Older guides mention ``ANTHROPIC_SMALL_FAST_MODEL`` for the background model; it is
deprecated in favour of ``ANTHROPIC_DEFAULT_HAIKU_MODEL``.

For a fully offline session add ``DISABLE_TELEMETRY=1``, ``DISABLE_ERROR_REPORTING=1``
and ``CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1``; Claude Code reads only whether
these are set, so any value works. LM Studio's integration page also suggests
``CLAUDE_CODE_ATTRIBUTION_HEADER=0``.

Inside Claude Code, ``/status`` shows which base URL and credential source are in
use — the first thing to check when something is off.

Per-project instead of per-shell
================================

If a project should always use the local model, put the variables in
``.claude/settings.json`` in that project (or ``~/.claude/settings.json`` for all
projects):

.. code-block:: json

   {
     "env": {
       "ANTHROPIC_BASE_URL": "http://localhost:1234",
       "ANTHROPIC_AUTH_TOKEN": "lmstudio",
       "ANTHROPIC_MODEL": "qwen-local",
       "ANTHROPIC_DEFAULT_HAIKU_MODEL": "qwen-local",
       "ANTHROPIC_DEFAULT_SONNET_MODEL": "qwen-local",
       "ANTHROPIC_DEFAULT_OPUS_MODEL": "qwen-local",
       "CLAUDE_CODE_MAX_CONTEXT_TOKENS": "32768"
     }
   }

A settings-file value wins over a shell export of the same variable, which is worth
remembering when a session ignores what you just exported.

On Windows and Linux
====================

The server side and the variables are the same; what differs is how the variables are
set. I have run this on macOS only; the notes below follow LM Studio's and Claude Code's
documentation.

- LM Studio has Windows and Linux builds with the same ``lms`` commands and the same
  port. On Linux the model runs through CUDA or Vulkan, and the memory figures above
  apply to the graphics card's memory rather than to unified memory.
- Claude Code installs natively on Windows 10 (1809) or newer from PowerShell with
  ``irm https://claude.ai/install.ps1 | iex`` or ``winget install Anthropic.ClaudeCode``;
  Git for Windows is recommended so that the agent has a Bash tool. In PowerShell the
  exports become

  .. code-block:: powershell

     $env:ANTHROPIC_BASE_URL = "http://localhost:1234"
     $env:ANTHROPIC_AUTH_TOKEN = "lmstudio"
     $env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "qwen-local"
     $env:ANTHROPIC_DEFAULT_SONNET_MODEL = "qwen-local"
     $env:ANTHROPIC_DEFAULT_OPUS_MODEL = "qwen-local"
     $env:CLAUDE_CODE_MAX_CONTEXT_TOKENS = "32768"
     claude --model qwen-local

  and last for that window. The ``settings.json`` above is identical on every platform
  (``%USERPROFILE%\.claude\settings.json`` for all projects) and is the better choice on
  Windows, because it sidesteps the shell question.
- Claude Code inside WSL with LM Studio on the Windows side: ``localhost`` in WSL 2 is
  not the Windows host unless WSL's mirrored networking mode is on
  (``networkingMode=mirrored`` in ``.wslconfig``). Otherwise enable *Serve on Local
  Network* in LM Studio's server settings and put the Windows host's address in
  ``ANTHROPIC_BASE_URL``. Installing Claude Code natively on Windows avoids this.

Step 4: Work
------------

.. code-block:: bash

   cd /path/to/project
   claude --model qwen-local

Ask it to inspect the repository, propose edits, run the tests, and review the diff
before you commit. Keep tasks small and concrete; local models do far better with
"add a ``--dry-run`` flag to this script" than with "clean up the project".

Troubleshooting
---------------

``Connection refused``
   Nothing listens on the port. ``lms server status``; start the server; confirm the
   port in ``ANTHROPIC_BASE_URL``.

Claude Code shows the login screen although ``curl`` works
   The credential variable is not set in the shell you launched ``claude`` from, or
   a settings file overrides it. ``echo $ANTHROPIC_AUTH_TOKEN``; check ``/status``.

A startup warning about two credential sources ("auth may not work as expected")
   Both ``ANTHROPIC_API_KEY`` and ``ANTHROPIC_AUTH_TOKEN`` are set. Keep one;
   LM Studio accepts either header.

``404`` or "model not found" in the middle of a session
   A background call used the ``haiku`` alias. Set ``ANTHROPIC_DEFAULT_HAIKU_MODEL``
   (and the sonnet/opus ones) to your local model as above.

``500 Error rendering prompt with jinja template``
   Followed by "Unknown StringValue filter: safe" or "Cannot apply filter trim to type:
   Undefined". The model file's chat template does not survive the tool definitions
   Claude Code sends; the simple ``curl`` works because it sends none. I hit this with a
   community GGUF of Qwen3-Coder. Download the model again from LM Studio's catalog
   (``lms get qwen/qwen3-coder-30b``), which uses a corrected template, or override the
   template under *My Models → Prompt Template*. Nothing on the Claude Code side is wrong.

``[claude-code:unrecognized_model]`` at startup, or "assumes a context window of 200k"
   Informational: Claude Code does not know the local model's window. Set
   ``CLAUDE_CODE_MAX_CONTEXT_TOKENS`` to the loaded context length.

"claude.ai connectors are disabled because ANTHROPIC_API_KEY or another auth source is set"
   Expected when ``ANTHROPIC_AUTH_TOKEN`` is set: the session uses the local
   credential and skips the claude.ai features that need your login. Harmless.

``400`` naming a token or context limit
   The loaded context is too small. Reload with ``--context-length 32768`` or more;
   ``lms ps`` shows the value in force.

The model explains what it would do but never edits a file
   No (working) tool calling. Switch to one of the models listed above.

The first answer takes a minute, later ones are fast
   Prompt processing of the ~20K-token system prompt. Normal; larger context and a
   bigger model make it longer.

Everything is slow
   The model does not fit comfortably. Use a smaller quantisation or model, lower the
   context length, close memory-hungry apps. ``lms log stream --source server`` and
   ``lms log stream --source model --filter output --stats`` show what the server is
   doing.

Summary
-------

1. ``lms load <model> --context-length 32768 --identifier qwen-local``
2. ``lms server start --port 1234``
3. ``export ANTHROPIC_BASE_URL=http://localhost:1234 ANTHROPIC_AUTH_TOKEN=lmstudio``,
   map the ``ANTHROPIC_DEFAULT_*_MODEL`` aliases to the local model and set
   ``CLAUDE_CODE_MAX_CONTEXT_TOKENS`` to the loaded context
4. ``claude --model qwen-local``

Related guides: :link-flat:`Claude Code with Ollama on macOS and Linux <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>`
and :link-flat:`OpenAI Codex CLI with a local model <{filename}/blog/2026-09-24-codex-cli-local-model-lm-studio-ollama.rst>`.

Sources: `LM Studio, Claude Code integration <https://lmstudio.ai/docs/integrations/claude-code>`_;
`LM Studio, Anthropic compatibility endpoints <https://lmstudio.ai/docs/developer/anthropic-compat>`_;
`Claude Code, connect to an LLM gateway <https://code.claude.com/docs/en/llm-gateway-connect>`_;
`Claude Code, model configuration <https://code.claude.com/docs/en/model-config>`_.
