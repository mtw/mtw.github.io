Four coding agents against ten local models on an exo cluster
##############################################################

:date: 2026-11-14
:tags: AI; tools
:category: howto
:section: guides
:bridge: tools
:slug: coding-agents-local-models-exo-cluster
:feedback: guide
:title: Claude Code, Codex, OpenCode and pi against ten local models on a two-Mac exo cluster
:summary: I ran Claude Code, Codex, OpenCode and pi against the ten models that are downloaded on my exo cluster (two Mac minis with 24 GB each), with the same one-line editing task for all of them, one model loaded at a time, and exo's runner states read after every run. The table shows which combinations completed the edit. The text explains the failures, which turned out to have four unrelated causes, i.e. two models that write the tool call as text instead of making it, the 6-bit gemma-4-31b, whose 24 GB of weights leave so little memory that a prompt of a few thousand tokens kills it, a problem specific to Codex with gemma 4, and ordinary mistakes by the models.
:description: Claude Code, Codex CLI, OpenCode and pi measured against ten local models on an exo cluster of two 24 GB Macs, with the causes of the failures taken apart.

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: series-note

   Local AI coding tools, a short series: :link-flat:`Claude Code with LM Studio <{filename}/blog/2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst>` · :link-flat:`Claude Code with Ollama <{filename}/blog/2026-09-24-run-claude-code-with-ollama.rst>` · :link-flat:`Codex CLI with a local model <{filename}/blog/2026-09-24-codex-cli-local-model-lm-studio-ollama.rst>` · :link-flat:`Claude Code for data analysis with a local model <{filename}/blog/2026-10-28-claude-code-csv-reproducible-analysis.rst>` · four agents against ten models (this post)

.. frame:: Workshop in preparation

   Measurements like these are what a half-day workshop for research groups is built on,
   for groups whose unpublished data and code must not leave their own machines. It has
   no date yet. The `waiting list at RNA Forecast <https://rnaforecast.com/training/?utm_source=michaelwolfinger&utm_medium=referral&utm_campaign=local-ai-tools&utm_content=agent-matrix#local-ai-tools>`_
   sends one e-mail when a first date exists, and nothing else.

In the :link-flat:`Codex post <{filename}/blog/2026-09-24-codex-cli-local-model-lm-studio-ollama.rst>`
of this series I wrote that Codex had taken a gemma model down on my exo cluster and
that I did not know why. Since then I have done the measurement properly, with every
model that is on the cluster, the four coding agents I use, the same small task for all
of them, and exo's own account of what happened to its runners after each run. The
result is a table of forty cells, and the failures in it turned out to be four unrelated
things which from the outside all looked the same, namely that the agent did not do what
it was asked. The table comes first, then the four causes one after the other, then
what I would run on this hardware, and at the end some notes on the measurement itself
for anyone who wants to repeat it.

The setup and the task
----------------------

The cluster consists of two Mac minis with 24 GB of memory each, pooled by `exo
<https://github.com/exo-explore/exo>`_ over a Thunderbolt link with RDMA. Every model
that supports it was run tensor-sharded across both machines (exo calls this the
``Tensor`` placement with the ``MlxJaccl`` backend, with one runner per machine). Only one model was loaded at a time, and its instance was deleted before the
next model was loaded, so that no run inherited memory pressure from the one before.

The models are the ten that happened to be downloaded on both nodes when I started,
between 8 and 31 GB of weights, which is a fair sample of what someone with this kind of
cluster would actually have around. The agents are Claude Code 2.1.323, which talks to
exo through its ``/v1/messages`` endpoint, Codex CLI 0.167.2, which uses
``/v1/responses``, and OpenCode 2.2.7 and pi 0.73.1, which both use
``/v1/chat/completions``. Each agent was configured the way its own documentation
describes, with the model id given on the command line.

The task is deliberately small. Every agent starts in a fresh git repository containing
one file, ``sample.txt``, with the three lines ``line one``, ``line two`` and
``line three``, and gets the instruction

.. code-block:: text

   In the file sample.txt, change the line 'line two' to 'line 2'.
   Edit the file in place. Do not print the file or ask questions.

A run counts as passed if the file is byte-identical to the expected result afterwards.
What the agent itself reports is recorded but plays no role in the verdict (the reason
for this becomes clear below). Each run had seven minutes.

After every run the harness read exo's ``/state`` endpoint and noted whether the runners
of the loaded instance were still ``Ready`` or ``Running``, or had gone to ``Failed``.
If a model's runners had died, the model was loaded again before the next agent got its
turn, so that one crash could not spoil the rest of the row.

This is the result:

.. code-block:: text

   model (weights)                    Claude Code    Codex           OpenCode     pi
   Llama-3.1-8B 8bit (8.3 GB)         text-call      text-call       text-call    text-call
   gpt-oss-20b MXFP4 (11.2 GB)        pass 23 s      runners died    pass 16 s    pass 6 s
   Qwen2.5-Coder-14B 8bit (14.6 GB)   text-call      text-call       text-call    text-call
   Huihui-Qwen3.5-27B 4bit (15.0 GB)  pass 128 s     pass 61 s       pass 84 s    pass 22 s
   gemma-4-31b 4bit (17.1 GB)         pass 158 s     runners died    pass 107 s   pass 15 s
   Huihui-Qwen3.5-9B 4bit (17.5 GB)   pass 51 s      pass 57 s       pass 51 s    pass 13 s
   Qwen3.5-35B-A3B 4bit (19.0 GB)     pass 47 s      wrong edit      pass 17 s    pass 9 s
   GLM-4.7-Flash 5bit (21.0 GB)       pass 55 s      pass 27 s       pass 31 s    pass 9 s
   gemma-4-31b 6bit (24.3 GB)         runners died   runners died    runners died pass 31 s
   gemma-4-31b 8bit (31.4 GB)         runners died   runners died    runners died runners died

Four of the ten models completed the edit with all four agents. pi was the fastest agent
on every model, usually by a factor of three to ten, which is no surprise since it sends
by far the smallest prompt. The failures in the remaining cells have four different
causes, and I take them in turn.

Two models that do not call tools
---------------------------------

Llama 3.1 8B and Qwen2.5-Coder 14B, both served through exo's chat template, never make
a tool call. Instead they write the call out as text, which is then the whole reply:

.. code-block:: text

   {"name": "edit", "parameters": {"path": "sample.txt", "oldString": "line two", "newString": "line 2"}}

Nothing is executed and the file stays as it was. All four agents nevertheless report
that the edit has been made. Codex gets the same thing in its own notation
(``<|python_tag|>{"name": "apply_patch", ...``) and OpenCode in yet another
(``<execute> tools.edit(...) </execute>``). There is nothing an agent can do about this
from its side. A model that behaves like this on your server is a chat model, whatever
the model card says about tool use.

Where the 6-bit gemma dies from the prompt size alone
-----------------------------------------------------

The 6-bit gemma-4-31b failed under three of the agents and passed under pi, and the
8-bit failed under all four. Before blaming the agents I sent the 6-bit plain chat
completions of increasing length, without tools and without any agent involved, and
read the runner states after each one:

.. code-block:: text

   prompt, approx. tokens    ~1,000   ~4,000   ~8,000   ~12,000   ~16,000
   gemma-4-31b 6bit          ok       died     died     died      died
   gemma-4-31b 4bit          ok       ok       ok       ok        ok

A prompt of about 4,000 tokens kills the runners of the 6-bit every time, on a freshly
loaded instance, whereas the 4-bit answers 16,000 tokens without any trouble. Every
coding agent except pi sends a system prompt plus tool schema that lies above the
6-bit's limit, which is exactly the pattern in the table above. On two 24 GB machines
the 6-bit gemma is therefore a chat model and the 8-bit cannot be used at all.
GLM-4.7-Flash, which at 21 GB is almost as large, passed with all four agents, so this
is a property of gemma's KV cache and not a general limit at around 20 GB of weights.

Codex with gemma 4
------------------

On the 4-bit gemma, which as just shown tolerates far more context than any agent
sends, Codex killed both runners within roughly thirty seconds of its first request, on
three separate loads, three times out of three. Claude Code, OpenCode and pi completed
the edit on the very same instance. Codex also took down the gpt-oss runners once, and
in another attempt on gpt-oss it hung for the full seven minutes without producing
anything.

This is not a general problem between Codex and exo. Codex passed on Huihui-Qwen3.5-27B,
on Huihui-Qwen3.5-9B and on GLM-4.7-Flash. Its failure on Qwen3.5-35B was an
ordinary mistake by the model (see the next section). What fails is the combination of
Codex with this particular model family, and Codex is the only one of the four agents
that uses exo's Responses endpoint.

There is one concrete suspect. Codex 0.169 puts a developer item at the front of the
Responses ``input`` that carries its so-called code-mode ``exec`` tool, a JavaScript tool
with which the model can compose the other tools, and exo rejects such a request
outright with HTTP 422. Codex 0.167, the version in the table, gets further than that.
I therefore repeated the gemma row with the feature switched off:

.. code-block:: text

   codex -c features.code_mode_host=false exec ...

   gemma-4-31b 4bit, feature on     died 31 s      died 32 s      died 32 s
   gemma-4-31b 4bit, feature off    alive, 185 s   alive, 273 s   died 239 s
   gpt-oss-20b, feature off         died 13 s

With the feature off the quick failure did not occur, and two of the three sessions ran
to the end, which no Codex session on this model had done before. Neither of them edited
the file, though. Both ran ``sed`` with a line break inside the substitute pattern and
stopped at the resulting error, and one of them reported success regardless. The third
session's runners died after four minutes. On gpt-oss nothing changed, and shortly
before the runners died Codex logged ``failed to parse function arguments: invalid
type: sequence, expected a string``, i.e. the model had returned an array where the
tool schema asks for a string.

The code-mode tool definition is therefore part of the cause, but not all of it. The
more interesting leftover is the ``sed`` with the line break in it. That mistake occurred
under Codex on two unrelated models, Qwen3.5-35B and gemma, and under no other agent
on any model. When two different models make the same error at the level of single
characters through one and the same client, the client's side of the exchange is the
place to look, in this case how the arguments of Codex's ``exec_command`` arrive through
exo's translation of the Responses API. That is what a logging proxy between Codex and
exo should be set up to capture. It is the next step.

Ordinary mistakes
-----------------

Two of the remaining failures are of the kind that a second attempt fixes. Qwen3.5-35B
under Codex ran ``sed -i 's/line two/line 2/' sample.txt`` with a line break inside the
quotes, got ``unterminated substitute pattern`` back and gave up. gpt-oss under
OpenCode once produced tool names with the markers of its Harmony format leaked into
them (``edit<|channel|>json``), which OpenCode rejected as an unknown tool, and on the
next load the same pair passed without incident. These are also the only failures in
the table that a better model or a longer prompt could have prevented.

Which models to use on two 24 GB Macs
-------------------------------------

For agentic work on this hardware, GLM-4.7-Flash 5bit, Qwen3.5-35B-A3B 4bit and the
two Huihui Qwen3.5 quantisations worked with every agent, and of these Qwen3.5-35B is
the fastest because only 3B of its parameters are active for any given token. The 4-bit
gemma-4-31b works with everything except Codex. The 6-bit gemma is usable for chat and
for nothing else, and Llama 3.1 8B and Qwen2.5-Coder 14B are not usable for agents at
all, at least not through this server. Among the agents, pi finishes the same task in
about a tenth of the time the others need, so for anything that fits into one or two
tool calls it is the one I would start.

Notes on the measurement itself
-------------------------------

The harness went through five revisions before the table above was trustworthy, and
each revision changed at least one column. Almost all of the problems were with the
agents rather than with the models. They are worth knowing about if you script any of
these tools.

- Every agent has to run in a git repository. Codex refuses to work outside one, and
  OpenCode and Claude Code use it to anchor their project.
- OpenCode takes its working directory from the ``PWD`` environment variable rather than
  from the directory the process actually runs in. A subprocess that sets the directory
  but inherits the parent's ``PWD`` therefore lets OpenCode work in the wrong place. In
  addition, ``opencode run`` attaches to a shared background service by default, a service that
  remembers the project of the first run. With ``--standalone --auto --archived``
  and an explicit ``PWD`` the OpenCode column became clean, with times a third to a half
  shorter.
- The agents need ``/dev/null`` on standard input. An inherited non-blocking stdin made
  Codex fail after zero seconds and cost Claude Code three seconds per run.
- A runner in state ``Running`` is alive. The only readiness that counts is a completion
  that actually comes back, not what the runner state says.
- exo offers a placement on one node when the other node is missing or when its memory
  has not yet been released after the previous delete. The harness has to insist on
  both runners and wait some twenty seconds between attempts, otherwise a degraded run
  passes as a normal one.
- ``codex exec --skip-git-repo-check`` writes a trust entry for every directory it runs
  in into ``~/.codex/config.toml``.

One lesson is more general than the others. What an agent says about its own work is no
measurement of it. Three of the ten models above produced, with each of the four
agents, a confident report that the edit had been made, over a file that had not
changed.
