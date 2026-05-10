What AI can and cannot do for RNA structure and RNA-protein modeling
####################################################################

:date: 2025-02-01
:modified: 2026-04-30
:tags: AI; RNA structure prediction; RNA-Protein interaction; 3D
:category: outreach
:slug: What-AI-Can-and-Cannot-Do-for-RNA-Structure-and-RNA-Protein-Modeling
:author: mtw
:summary: AI affects RNA structure and RNA-protein modeling in very different ways depending on whether the task concerns ranking, geometry generation, or mechanistic inference, and whether the output remains anchored in physics and experiment.
:title: What AI can and cannot do for RNA structure and RNA-protein modeling
:description: A researcher’s view on which AI-based models address ranking or geometry generation in RNA biology, and where mechanistic inference still depends on physical and experimental constraints.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/figures/RNP_complex_network1.webp
          :alt: RNA protein complex embedded in a network
          :figclass: m-figure m-flat


AI now appears in several distinct parts of RNA biology, including
sequence annotation, structure scoring, kinetics approximation, and the
generation of candidate models for RNA-protein complexes. Treating
"AI for RNA" as a single activity obscures the fact that these tasks
operate at different levels of inference.

One distinction that matters is between output generation and
interpretation. A model may produce a plausible structure, a ranking,
or a strong benchmark score without resolving the biological
uncertainty that motivated the analysis. :link-flat:`Caveats to deep learning approaches to RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>` makes that point very clearly. Good performance on familiar datasets
does not guarantee generalization to new sequence families, new
experimental conditions, or regulatory RNAs that occupy multiple
states.

Another distinction is between coordinate generation and mechanistic
explanation. In RNA-protein systems, AI-derived models can place domains
sensibly, suggest contact regions, and reduce the search space. They do
not necessarily settle whether the proposed geometry explains
specificity, accessibility, competition, or function. :link-flat:`A structural refinement technique for protein-RNA complexes using a combination of AI-based modeling and flexible docking <{filename}/blog/2023-06-09-A-Structural-Refinement-Technique-for-Protein-RNA-Complexes-Using-Combination-of-AI-based-Modeling-and-Flexible-Docking-A-Study-of-Musashi-1-Protein.rst>` is relevant here because refinement, docking, and consistency checks
still change the conclusion.

The Musashi line of work makes this especially clear. :link-flat:`Theoretical studies on RNA recognition by Musashi1 RNA-binding protein <{filename}/blog/2022-07-26-Theoretical-studies-on-RNA-recognition-by-Musashi1-RNA-binding-protein.rst>` asks which motifs bind better and why. :link-flat:`From Structure to Function: Computational Insights into Musashi-RNA Complexes <{filename}/blog/2025-01-01-From-Structure-to-Function-Computational-Insights-into-Musashi-RNA-Complexes.rst>` then steps back and asks how those structural observations connect to a broader functional picture. AI enters that workflow at the model-generation stage, not at the level of final interpretation.

Kinetics offers a similar lesson. :link-flat:`KinPFN: Bayesian Approximation of RNA Folding Kinetics <{filename}/blog/2025-01-01-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst>` is interesting precisely because it does not pretend to solve folding
physics from scratch. It uses AI as an approximation layer on top of a
physically meaningful problem.

The most convincing use cases are therefore those in which AI addresses
ranking, initialization, or approximation, while the mechanistic
interpretation remains anchored in physics, experiment, or comparative
evidence. Confidence scores alone are much less informative than that
broader context.

For researchers and teams, the practical issue is usually which part of
the inference has actually been automated, and which part still depends
on stronger stress testing or on additional evidence. That judgment
becomes especially difficult when the output looks polished and the
project is under time pressure. In that situation, a careful review of
the modelling assumptions and likely failure modes is usually more
valuable than enthusiasm. My :link-flat:`services page <{filename}/services.rst>` describes the formats I use for that kind of focused
review and advisory support.
