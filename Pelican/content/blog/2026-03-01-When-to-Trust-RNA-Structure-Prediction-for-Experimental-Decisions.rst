When to trust RNA structure prediction for experimental decisions
#################################################################

:date: 2026-03-01
:modified: 2026-05-01
:tags: RNA structure prediction; ViennaRNA; SHAPE; AI; RNA design
:category: outreach
:slug: When-to-trust-RNA-structure-prediction-for-experimental-decisions
:author: mtw
:summary: RNA structure prediction is most useful when it narrows the experimental space, exposes uncertainty clearly, and helps determine when the available structural evidence is sufficient for the next step.
:title: When to trust RNA structure prediction for experimental decisions
:description: A practical guide to when RNA secondary structure prediction is reliable enough to support experimental choices, and when additional probing, comparative evidence, or more careful modeling is needed.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

The usefulness of RNA structure prediction is often discussed in terms
of nominal accuracy or benchmark performance. For experimental work, the
more relevant issue is narrower. One needs to know under which
conditions a predicted structure can support construct design,
mutational analysis, or the choice of a follow-up experiment.

In many practical settings, prediction is already useful when it
reduces the set of plausible structural alternatives. A unique
secondary structure is not required. It is sufficient that the
structurally relevant features remain stable enough to constrain the
next step.

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

Confidence increases when a structural conclusion remains stable under
several, partly independent lines of evidence.
:link-flat:`SHAPE directed RNA folding with the ViennaRNA Package <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>` is instructive in that regard. SHAPE reactivities do not reveal a finished
secondary structure. They constrain the set of structures that remain
plausible once nucleotide flexibility is taken into account. When the
sequence-only model and the probing data support the same structural
features, the prediction becomes considerably more useful for
experimental planning.

The current machine-learning literature changes the tooling but not the
underlying problem. As discussed in :link-flat:`Caveats in deep learning for RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`, strong performance on benchmark sets is not equivalent to robust
structural inference. Sequence-only neural models therefore require the
same caution as any other predictor when the sequence class is unusual,
when the mechanism depends on context, or when the experimental cost of
a wrong inference is high.

The useful questions are more specific than any headline performance
number. One needs to know whether the relevant structural feature
persists under modest perturbations of sequence or model assumptions,
whether competing structures remain close enough in free energy to alter
the biological interpretation, and whether probing, comparative, or
biochemical data support the same conclusion. The threshold also
depends on cost. Weak support may be acceptable when the next
experiment is cheap, but not when a design cycle is costly or when a
broader biological claim rests on the result.

Kinetics therefore keeps reappearing in design-oriented problems.
A construct can appear plausible at equilibrium and still behave
differently once the folding pathway becomes mechanistically relevant. I
discuss that in more detail in :link-flat:`Why kinetic folding matters in RNA design <{filename}/blog/2025-01-20-Why-Kinetic-Folding-Matters-in-RNA-Design.rst>`.
Equilibrium folding remains informative, but
some experimental decisions depend on aspects of the system that a
single static structure cannot represent adequately.

RNA structure prediction is most useful when it reduces the experimental
space in a transparent way and when independent evidence supports the
same structural interpretation. It deserves more caution when the
mechanism is strongly context-dependent, when structural alternatives
remain poorly resolved, or when the cost of a wrong inference is
substantial.

For groups working near that boundary between useful prediction and
overinterpretation, an external technical review can be helpful. The
difficulty is rarely the execution of the software itself. It is the
judgment of which structural claims are already strong enough to support
action and which still require an additional layer of evidence. That is
the kind of question I address in :link-flat:`design reviews and advisory work </services>`.
