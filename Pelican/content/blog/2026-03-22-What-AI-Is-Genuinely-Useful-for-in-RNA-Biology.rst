What AI is genuinely useful for in RNA biology
##############################################

:date: 2026-03-22
:modified: 2026-05-01
:tags: AI; RNA structure prediction; RNA folding kinetics; RNA-Protein interaction; virus bioinformatics
:category: outreach
:status: skip
:slug: What-AI-Is-Genuinely-Useful-for-in-RNA-Biology
:author: mtw
:summary: AI enters RNA biology at several distinct levels, including candidate ranking, kinetics approximation, geometry generation, and large-scale classification, but the underlying biological question remains different in each case.
:title: What AI is genuinely useful for in RNA biology
:description: A view of how AI operates across candidate ranking, kinetics approximation, structural modeling, and viral-genomic classification, and why those tasks should not be collapsed into a single claim about “AI for RNA”.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

AI has become part of everyday conversation in RNA biology, but the
term covers very different kinds of work. Sequence annotation,
structure prediction, kinetics approximation, interface refinement, and
genomic surveillance do not pose the same biological problem and should
not be judged by the same standard.

The central issue is therefore not whether AI "works" in some generic
sense, but which level of inference it addresses in a given problem.

Candidate prioritization is one example. If a project already has a
meaningful objective function and a sensible representation of
uncertainty, AI can compare far more possibilities than exhaustive
simulation or manual review would allow. :link-flat:`KinPFN for RNA folding kinetics <{filename}/blog/2025-01-01-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst>` is relevant in that respect. The method does not claim to
rediscover folding physics from sequence alone. It acts as an
approximation layer on top of an existing kinetics problem.

Structural refinement is another. In protein-RNA work, AI-derived
models can generate starting geometries, but they rarely settle the
biological question on their own. Their role appears only after they
have been passed into a more explicit refinement workflow. That is the
theme of :link-flat:`What AI can and cannot do for RNA structure and RNA-protein modeling <{filename}/blog/2025-02-01-What-AI-Can-and-Cannot-Do-for-RNA-Structure-and-RNA-Protein-Modeling.rst>` and the related Musashi studies, especially :link-flat:`RNA-protein complex refinement using AI modeling and docking <{filename}/blog/2023-06-09-A-Structural-Refinement-Technique-for-Protein-RNA-Complexes-Using-Combination-of-AI-based-Modeling-and-Flexible-Docking-A-Study-of-Musashi-1-Protein.rst>`.

AI can also enter at the organizational level rather than the
mechanistic one. Viral genomics is a good example. In :link-flat:`Automated lineage designation from viral genomic data <{filename}/blog/2024-02-12-A-framework-for-automated-scalable-designation-of-viral-pathogen-lineages-from-genomic-data.rst>`, the central challenge is to keep a classification system usable
once the number of genomes becomes too large for purely manual
nomenclature. That kind of problem is well suited to heuristic or
learning-assisted automation, provided the rules remain interpretable.

The more difficult cases are those in which the relevant mechanism is
only weakly constrained. RNA secondary structure prediction remains the
clearest example. As discussed in :link-flat:`Caveats in deep learning for RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`, high benchmark performance may say more about dataset
familiarity than about structural understanding.

Several questions are often conflated. A model may produce a plausible
output and still fail to generalize beyond familiar training
distributions. It may generalize reasonably well and still leave the
biological question unresolved.

In practical RNA work, AI often enters in relatively narrow parts of
the analysis. It can shorten an expensive inference cycle, propose
models worth checking, or reduce a large candidate space to something
that can be examined more carefully by a human or by a physical model.

Classical modeling and experiment are not being left behind. In most of
the RNA problems I find convincing, AI operates within a framework that
is still defined by thermodynamics, comparative reasoning, kinetic
analysis, or explicit structural constraints. The same point underlies
:link-flat:`When to trust RNA structure prediction for experimental decisions <{filename}/blog/2026-03-01-When-to-Trust-RNA-Structure-Prediction-for-Experimental-Decisions.rst>`.

AI changes RNA biology most clearly when the underlying problem has
already been formulated in a structurally or mechanistically meaningful
way. It changes much less when the underlying question remains vague.
