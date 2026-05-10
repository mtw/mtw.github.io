When to trust RNA structure prediction for experimental decisions
#################################################################

:date: 2026-03-01
:modified: 2026-05-01
:tags: RNA structure prediction; ViennaRNA; SHAPE; AI; RNA design
:category: outreach
:slug: When-to-trust-RNA-structure-prediction-for-experimental-decisions
:author: mtw
:summary: RNA structure prediction becomes most useful when it helps rule out bad ideas, prioritize experiments, and expose uncertainty clearly. The key question is not whether a model outputs a fold, but whether the prediction is strong enough to support the next decision.
:title: When to trust RNA structure prediction for experimental decisions
:description: A practical guide to when RNA secondary structure prediction is reliable enough to support experimental choices, and when additional probing, comparative evidence, or more careful modeling is needed.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

The usefulness of RNA structure prediction is often discussed in terms
of nominal accuracy or benchmark performance. For experimental work,
however, the more relevant question is narrower. Under what conditions
does a predicted structure provide enough support for the next decision,
whether that decision concerns construct design, mutational analysis, or
the choice of a follow-up experiment.

This immediately shifts the standard. In most practical settings, a
prediction does not have to identify one exact structure in order to be
useful. It has to delimit a plausible structural space, expose the
relevant uncertainties, and rule out enough weak alternatives that an
experimental choice becomes more disciplined. The critical point is
therefore not whether a folding algorithm returns a structure, but
whether the current combination of evidence is strong enough that acting
on the prediction is preferable to remaining uncertain.

There are many settings in which classical RNA structure prediction
still performs well by that standard. Compact RNAs, shorter structural
motifs, and systems with a reasonably dominant conformational regime are
often amenable to thermodynamic analysis. The same applies when the aim
is not to assert one final fold, but to identify stable helices,
candidate pairing regions, or structural alternatives that can be taken
forward experimentally. In such cases, ensemble properties are often
more informative than the minimum-free-energy structure alone.

The situation becomes less straightforward once the biology depends more
strongly on context. Ligand binding, protein occupancy,
co-transcriptional folding, long-range interactions, and metastable
states all complicate the interpretation of a static secondary
structure. This is one reason :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>` remains such a useful review. It makes clear that thermodynamic models
become substantially more informative when combined with experimental
evidence, but also that the additional data do not remove the need for
structural interpretation.

In practice, confidence increases most when a structural conclusion
remains stable under several, partly independent lines of evidence.
:link-flat:`SHAPE directed RNA folding with the ViennaRNA Package <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>` is instructive in that regard. SHAPE reactivities do not reveal a finished
secondary structure. They constrain the set of structures that remain
plausible once nucleotide accessibility is taken into account. When the
sequence-only model and the probing data support the same structural
features, the prediction becomes considerably more useful for
experimental planning.

The current machine-learning literature changes the tooling but not the
underlying inferential problem. As discussed in :link-flat:`Caveats in deep learning for RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`, strong performance on benchmark sets is not equivalent to robust
structural understanding. Sequence-only neural models therefore require
the same caution as any other predictor when the sequence class is
unusual, when the relevant mechanism depends on context, or when the
experimental cost of a wrong inference is high.

From that perspective, several practical criteria become more relevant
than any headline performance number. One is whether the predicted
feature remains stable under modest perturbations of the sequence or the
model assumptions. Another is whether competing structures remain close
enough in free energy to alter the biological interpretation. A third is
whether probing, comparative, or biochemical evidence moves the analysis
consistently in one direction. Finally, the threshold for action depends
on the cost of being wrong. A weaker prediction may be acceptable when
the next experiment is cheap. The same level of support may be
inadequate when a design cycle is costly or when a broader biological
claim rests on the result.

This is also why kinetics keeps reappearing in design-oriented problems.
A construct can appear plausible at equilibrium and still behave
differently once the folding pathway becomes mechanistically relevant. I
discuss that in more detail in :link-flat:`Why kinetic folding matters in RNA design <{filename}/blog/2025-01-20-Why-Kinetic-Folding-Matters-in-RNA-Design.rst>`.
The point is not that equilibrium folding is uninformative, but that
some experimental decisions depend on aspects of the system that a
single static structure cannot represent adequately.

The practical conclusion is therefore rather modest. RNA structure
prediction is most trustworthy when it narrows the experimental space in
a transparent way, when independent evidence points toward the same
structural interpretation, and when the remaining uncertainty has been
made explicit. It deserves more caution when the relevant mechanism is
context-heavy, when structural alternatives remain poorly resolved, or
when the cost of a wrong inference is substantial.

For groups working near that boundary between useful prediction and
overinterpretation, an external technical review can be helpful. The
difficulty is rarely the execution of the software itself. It is the
judgment of which structural claims are already strong enough to support
action and which still require an additional layer of evidence. That is
the kind of question I address in :link-flat:`design reviews and advisory work </services>`.
