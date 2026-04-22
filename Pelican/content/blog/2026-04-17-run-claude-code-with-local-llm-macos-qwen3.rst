How to Run Claude Code with a Local LLM on Apple Silicon
########################################################

:date: 2026-04-17
:modified: 2026-04-22
:tags: AI, Agents
:category: howto
:slug: claude-code-local-llm-apple-silicon
:author: mtw
:title: How to Run Claude Code with a Local LLM on Apple Silicon
:summary: Configure Claude Code to use a local model served by LM Studio on Apple Silicon, with a practical setup based on LM Studio's Anthropic-compatible API.
:description: A practical guide to running Claude Code against a local LLM served by LM Studio on Apple Silicon.

This guide shows you how to run Claude Code with a locally hosted large language model on Apple Silicon. The supported integration path is to let LM Studio expose an Anthropic-compatible API endpoint and then point Claude Code at that local endpoint via environment variables.

The examples below use LM Studio on ``localhost:1234`` and a locally loaded model with a 32K context window.

Prerequisites
-------------

- A Mac with Apple Silicon.
- `LM Studio <https://lmstudio.ai/>`_ installed.
- ``claude`` installed.
- A local model downloaded or imported into LM Studio.
- Enough available RAM for the model you want to run.

Install Claude Code
-------------------

Install Claude Code using one of the current supported methods.

Native install:

.. code-block:: bash

   curl -fsSL https://claude.ai/install.sh | bash

Or via Homebrew:

.. code-block:: bash

   brew install --cask claude-code

After installation, verify that the CLI is available:

.. code-block:: bash

   claude --version
   claude doctor

Part 1: Prepare LM Studio
-------------------------

Start LM Studio
===============

Open LM Studio at least once. Then verify that the ``lms`` CLI is available in your shell.

Check that ``lms`` is installed:

.. code-block:: bash

   lms --help

If this command is not found, follow the LM Studio CLI setup/bootstrap step from the LM Studio documentation and then reopen your shell.

List locally available models:

.. code-block:: bash

   lms ls

If your model files were downloaded outside LM Studio, you can import them:

.. code-block:: bash

   lms import /path/to/model.gguf

Load a Model with a 32K Context Window
======================================

Load your chosen model into memory and set the context length explicitly.

If you want to estimate memory usage before loading:

.. code-block:: bash

   lms load --estimate-only <model_key> --context-length 32768

.. code-block:: bash

   lms load <model_key> --context-length 32768

You can also assign a stable identifier for API use:

.. code-block:: bash

   lms load <model_key> --context-length 32768 --identifier qwen-local

To see which models are currently loaded:

.. code-block:: bash

   lms ps

Start the Local Server
======================

Start LM Studio’s local server:

.. code-block:: bash

   lms server start --port 1234

Check server status:

.. code-block:: bash

   lms server status

At this point, LM Studio serves an Anthropic-compatible Messages API on ``http://localhost:1234/v1/messages``.

Part 2: Point Claude Code at LM Studio
--------------------------------------

Configure Environment Variables
===============================

Set Claude Code to use your local LM Studio server:

.. code-block:: bash

   export ANTHROPIC_BASE_URL=http://localhost:1234
   export ANTHROPIC_AUTH_TOKEN=lmstudio

If LM Studio’s ``Require Authentication`` option is enabled, replace ``lmstudio`` with your LM Studio API token.

When using ``ANTHROPIC_BASE_URL`` plus ``ANTHROPIC_AUTH_TOKEN`` against LM Studio, Claude Code authenticates against the local endpoint and does not need the usual browser login flow for that session.

Choose the Model
================

You can select the model when launching Claude Code:

.. code-block:: bash

   claude --model qwen-local

If you did not assign a custom identifier, use the loaded model name that LM Studio exposes.

Alternatively, set the model via an environment variable:

.. code-block:: bash

   export ANTHROPIC_MODEL=qwen-local
   claude

Part 3: Test the Local Endpoint
-------------------------------

Before starting Claude Code, test LM Studio directly against the Anthropic-compatible endpoint.

.. code-block:: bash

   curl http://localhost:1234/v1/messages \
     -H "content-type: application/json" \
     -H "x-api-key: lmstudio" \
     -d '{
       "model": "qwen-local",
       "max_tokens": 128,
       "messages": [
         {
           "role": "user",
           "content": "Write a one-line hello message."
         }
       ]
     }'

If this request succeeds, Claude Code should be able to use the same local server.

Part 4: Run Claude Code in a Project
------------------------------------

Start Claude Code inside your project directory:

.. code-block:: bash

   cd /path/to/your/project
   claude --model qwen-local

Typical workflow:

1. Ask Claude Code to inspect files in the repository.
2. Let it propose or apply edits.
3. Run your local build or test commands.
4. Review diffs before committing changes.

For example, in a Pelican project:

.. code-block:: bash

   pelican content

And then commit as usual:

.. code-block:: bash

   git add .
   git commit -m "Update article"

Troubleshooting
---------------

Claude Code cannot connect
==========================

Check that the LM Studio server is running:

.. code-block:: bash

   lms server status

Check that the model is loaded:

.. code-block:: bash

   lms ps

Check that the environment variables are set in the same shell where you launch ``claude``:

.. code-block:: bash

   echo "$ANTHROPIC_BASE_URL"
   echo "$ANTHROPIC_AUTH_TOKEN"

Responses are slow
==================

Agentic coding workloads are context-heavy. A local model may perform noticeably better with a larger context window. A practical starting point is around 25K tokens or more, and 32K is a reasonable target if your hardware can support it.

If performance is poor:

- Try a smaller or more coding-oriented model.
- Reduce other RAM-heavy workloads.
- Lower the context length if the model does not fit comfortably.
- Test a shorter prompt first to verify baseline responsiveness.

Need server or prompt diagnostics
=================================

Stream LM Studio logs:

.. code-block:: bash

   lms log stream --source server

Stream model input and output:

.. code-block:: bash

   lms log stream --source model --filter input,output

Include prediction stats when available:

.. code-block:: bash

   lms log stream --source model --filter output --stats

Notes
-----

This setup uses LM Studio’s Anthropic-compatible ``/v1/messages`` endpoint. It does **not** require a custom JSON provider file, and it does **not** use the old ``/v1/completions`` integration pattern.

If you want a persistent setup, you can place the same environment variables in your shell profile, for example ``~/.zshrc``:

.. code-block:: bash

   export ANTHROPIC_BASE_URL=http://localhost:1234
   export ANTHROPIC_AUTH_TOKEN=lmstudio
   export ANTHROPIC_MODEL=qwen-local

Summary
-------

With LM Studio serving a local model through its Anthropic-compatible Messages API and Claude Code pointed at that local endpoint, you can run a local-inference coding workflow on Apple Silicon.

In short, the essential steps are:

1. Load a model in LM Studio with your desired context length.
2. Start the LM Studio local server.
3. Set ``ANTHROPIC_BASE_URL`` and ``ANTHROPIC_AUTH_TOKEN``.
4. Launch Claude Code with ``--model`` or ``ANTHROPIC_MODEL``.
