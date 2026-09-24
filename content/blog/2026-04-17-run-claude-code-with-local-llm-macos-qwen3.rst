Run Claude Code with LM Studio: a local LLM on Apple Silicon
############################################################

:date: 2026-04-17
:modified: 2026-09-24
:tags: AI; tools
:category: howto
:section: guides
:slug: claude-code-local-llm-apple-silicon
:title: Run Claude Code with LM Studio: a local LLM on Apple Silicon
:summary: Connect Claude Code to LM Studio's Anthropic-compatible endpoint and run a local model on Apple Silicon: setup, model choice, context length, and the errors you will actually meet.
:description: How to connect Claude Code to LM Studio with ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN, run a local LLM on Apple Silicon, and fix the common errors.

.. role:: link-flat(link)
  :class: m-flat m-text

Claude Code can talk to any server that speaks Anthropic's Messages API, and since
version 0.4.1 (January 2026) LM Studio serves exactly that on ``localhost:1234``. Two
environment variables point Claude Code at it; no proxy, no provider file, no
translation layer. This guide covers the setup on a Mac with Apple Silicon, how to
choose a model and context length that actually work with an agent, and the failure
modes I ran into. It was first written in April 2026 and revised in September 2026 for
the current LM Studio and Claude Code behaviour.

I use this for the same reason many scientists will: unpublished sequence data and
manuscripts should not leave the machine, and a local model costs nothing per token.
The trade-off is capability. A 20–30B local model is a competent assistant for scripts,
refactoring, and documentation; it is not a substitute for the frontier models on large
multi-file tasks.

Prerequisites
-------------

- A Mac with Apple Silicon and enough unified memory for the model you want (see
  "Choosing a model" below; 32 GB is comfortable, 16 GB works with small models).
- `LM Studio <https://lmstudio.ai/>`_ 0.4.1 or newer, opened at least once.
- Claude Code: ``curl -fsSL https://claude.ai/install.sh | bash`` or
  ``brew install --cask claude-code``, then ``claude --version``.

Step 1: Load a model in LM Studio
---------------------------------

LM Studio ships a command-line tool, ``lms``. If your shell does not find it, run the
bootstrap step from the LM Studio app (Developer tab) and reopen the terminal.

.. code-block:: bash

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
  the best balance I have found for agentic work.
- ``openai/gpt-oss-20b`` (about 14 GB; LM Studio's and Ollama's default suggestion;
  needs 16 GB of memory and more with a large context).
- ``ibm/granite-4-micro`` for small machines — usable for simple edits, not more.

Step 2: Start the server
------------------------

.. code-block:: bash

   lms server start --port 1234
   lms server status

The Anthropic-compatible endpoint is ``http://localhost:1234/v1/messages``. Check it
before involving Claude Code:

.. code-block:: bash

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
- ``--model qwen-local`` selects the model for this session; ``ANTHROPIC_MODEL`` does
  the same from the environment.

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
       "ANTHROPIC_DEFAULT_OPUS_MODEL": "qwen-local"
     }
   }

A settings-file value wins over a shell export of the same variable, which is worth
remembering when a session ignores what you just exported.

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
3. ``export ANTHROPIC_BASE_URL=http://localhost:1234 ANTHROPIC_AUTH_TOKEN=lmstudio``
   and map the ``ANTHROPIC_DEFAULT_*_MODEL`` aliases to the local model
4. ``claude --model qwen-local``

Related guides: :link-flat:`Claude Code with Ollama on macOS and Linux <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>`
and :link-flat:`OpenAI Codex CLI with a local model <{filename}/blog/2026-09-24-codex-cli-local-model-lm-studio-ollama.rst>`.

Sources: `LM Studio, Claude Code integration <https://lmstudio.ai/docs/integrations/claude-code>`_;
`LM Studio, Anthropic compatibility endpoints <https://lmstudio.ai/docs/developer/anthropic-compat>`_;
`Claude Code, connect to an LLM gateway <https://code.claude.com/docs/en/llm-gateway-connect>`_;
`Claude Code, model configuration <https://code.claude.com/docs/en/model-config>`_.
