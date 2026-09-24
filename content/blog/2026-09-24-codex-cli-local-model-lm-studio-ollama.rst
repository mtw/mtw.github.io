Run OpenAI Codex CLI with a local model (LM Studio or Ollama)
#############################################################

:date: 2026-09-24
:tags: AI; tools
:category: howto
:section: guides
:slug: codex-cli-local-model-lm-studio-ollama
:title: Run OpenAI Codex CLI with a local model via LM Studio or Ollama
:summary: Codex CLI has a built-in local mode. One flag runs it against LM Studio or Ollama; a profile in config.toml makes the choice permanent. Setup, models, context length, and the Responses-API caveat.
:description: How to run OpenAI's Codex CLI against a local model with --oss or a config.toml profile, using LM Studio or Ollama, and which models and contexts work.

.. role:: link-flat(link)
  :class: m-flat m-text

Codex, OpenAI's terminal coding agent, ships with a local mode: ``codex --oss`` talks
to a local server instead of OpenAI's API. Both LM Studio and Ollama support it out of
the box, so the setup is even shorter than for Claude Code. What differs from the
Claude Code guides is the protocol: Codex uses OpenAI's *Responses* API, not the older
Chat Completions API, and it is hungrier for context.

Prerequisites
-------------

- Codex CLI: ``npm install -g @openai/codex`` (``codex --version`` to confirm).
- LM Studio 0.4 or newer, or Ollama 0.14 or newer.
- A model with tool calling and, for Codex, a large context: Ollama recommends "at
  least 64k tokens for Codex", LM Studio "more than ~25k". Memory follows the model:
  ``gpt-oss:20b`` needs about 16 GB, ``qwen3-coder`` about 19 GB; ``gpt-oss:120b``
  is a 65 GB download meant for an 80 GB GPU or a large-memory Mac.

With LM Studio
--------------

.. code-block:: bash

   lms load openai/gpt-oss-20b --context-length 65536
   lms server start --port 1234
   codex --oss                          # defaults to openai/gpt-oss-20b
   codex --oss -m qwen/qwen3-coder-30b  # any other loaded model

Codex talks to ``http://localhost:1234/v1/responses``. If the model is not loaded,
LM Studio loads it on first use with the server's default context, which is usually too
small; load it yourself with ``--context-length`` as above.

With Ollama
-----------

.. code-block:: bash

   OLLAMA_CONTEXT_LENGTH=65536 ollama serve     # in one terminal (or the app setting)
   ollama pull gpt-oss:20b
   codex --oss -m gpt-oss:20b                   # in another

Ollama also offers ``ollama launch codex``, which writes a profile for you and starts
Codex. The context-length note from the
:link-flat:`Ollama guide for Claude Code <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>`
applies unchanged: on a laptop Ollama's default context is 4K, and Codex needs far more.

Make it permanent with a profile
--------------------------------

``~/.codex/config.toml`` can hold a provider and a profile so that ``codex --profile
local`` does the right thing without flags:

.. code-block:: toml

   [model_providers.lmstudio]
   name = "LM Studio"
   base_url = "http://localhost:1234/v1"
   wire_api = "responses"

   [model_providers.ollama]
   name = "Ollama"
   base_url = "http://localhost:11434/v1"
   wire_api = "responses"

   [profiles.local]
   model_provider = "lmstudio"
   model = "openai/gpt-oss-20b"

   [profiles.local-ollama]
   model_provider = "ollama"
   model = "gpt-oss:20b"

Then ``codex --profile local`` or ``codex --profile local-ollama``. ``wire_api =
"responses"`` is the important line: a provider entry without it, or an old server
that only implements Chat Completions, answers Codex's requests with 404.

What to expect
--------------

The 20B models handle scoped tasks — a new function with tests, a refactor within a
file, a script — and get lost in large multi-file changes. Give Codex a small,
verifiable task, let it run the tests, and read the diff. If a model produces plans
but no edits, it lacks tool calling; switch models.

Related: :link-flat:`Claude Code with LM Studio on Apple Silicon <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>`
and :link-flat:`Claude Code with Ollama <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>`.

Sources: `LM Studio, Codex integration <https://lmstudio.ai/docs/integrations/codex>`_;
`Ollama, Codex CLI integration <https://docs.ollama.com/integrations/codex>`_;
`Ollama library, gpt-oss <https://ollama.com/library/gpt-oss>`_ and
`qwen3-coder <https://ollama.com/library/qwen3-coder>`_.
