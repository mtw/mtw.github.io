Michael T. Wolfinger's Research
###############################
:title: Research | Michael T. Wolfinger
:summary: Research by Michael T. Wolfinger on RNA structure, chemical probing, viruses, and structure-aware design
:description: Research by Michael T. Wolfinger on computational RNA biology, RNA structure, SHAPE and chemical probing interpretation, viral non-coding RNAs, and structure-aware design.
:extrahead: mtw_ldjson

:breadcrumb: / Home

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: link-sup(link)
  :class: m-flat m-text m-footnote

My research is concerned with the role of RNA structure in biological function, regulation, and design. I work on computational methods for RNA secondary and tertiary structure prediction, folding kinetics, RNA-protein recognition, synthetic RNA design, and structured viral RNAs. Across these areas, the central question is how far computation can take us when structural information is treated as mechanistically informative rather than as a decorative annotation on top of sequence.

That work sits at the interface of method development and application. Some projects are driven by basic questions in RNA folding or RNA-protein interaction, others by comparative virology or translational RNA biology. In each case, I am interested in models that remain interpretable and that support biological judgment. Thermodynamic folding models, comparative sequence analysis, molecular simulation, chemical probing data, and machine learning all have their place, but none of them is sufficient on its own. A recurring theme in my work is how these sources of evidence can be combined without losing sight of mechanism.

Research Themes
===============

Several lines of work have remained central over the years.

RNA structure prediction remains one of them. I am interested in both
secondary and tertiary structure, especially in settings where purely
sequence-based inference is not enough. This includes the principled
use of chemical probing data such as SHAPE, SHAPE-MaP, and DMS-based
workflows, as well as comparative evidence in families where structure
is conserved more clearly than primary sequence.

Folding kinetics is another. RNA molecules are not defined by a single
minimum-energy structure, and many regulatory or designed systems
depend on how the folding process unfolds in time. This is particularly
relevant for co-transcriptional folding, ligand-controlled RNAs, and
design problems where local alternatives or metastable states are part
of the mechanism rather than a nuisance.

Synthetic RNA design provides a natural extension of these questions.
Here the challenge is not only to predict what a sequence might do, but
to decide which sequence representations are good enough to support
experimental decisions. That includes design logic, accessibility,
kinetic effects, and the interpretation of structure-guided constraints
before constructs are taken forward.

Comparative RNA virology has become a major application area. Much of
this work focuses on conserved structured elements in flaviviral and
related genomes, including xrRNAs, long-range interactions, and
untranslated regions whose architecture is preserved even where raw
sequence similarity is weak. These systems are useful both biologically
and methodologically, because they expose the limits of sequence-only
thinking.

I also work on RNA-protein interactions and structure-guided modelling
in systems where RNA recognition cannot be understood from motif
matching alone. This includes the use of molecular modelling and
simulation to connect predicted structures with plausible interaction
geometries and functional interpretation.

Selected projects use machine learning where it offers a clear
advantage, for example in kinetic approximation or structure-guided
analysis. The emphasis is not on AI for its own sake, but on problems
where learned models can accelerate or refine a well-defined RNA
question without replacing physical or mechanistic reasoning.

Current Focus Areas
===================

.. raw:: html

   <ul>
     <li>RNA secondary and tertiary structure prediction informed by thermodynamics, probing data, and comparative analysis</li>
     <li>co-transcriptional folding, metastable structure, and kinetic modelling in regulatory and designed RNAs</li>
     <li>structure-aware RNA design, especially in contexts where experimental follow-up is costly or decision-critical</li>
     <li>comparative analysis of structured viral RNAs, with a focus on flaviviral untranslated regions and exoribonuclease-resistant elements</li>
     <li>RNA-protein interaction modelling and machine-learning methods for well-scoped RNA inference problems</li>
   </ul>

The :link-flat:`publication list <{filename}/publications.rst>` gives the formal record of this work. Many papers are also discussed in more detail on the :link-flat:`blog </blog/>`, where methodological and biological context can be developed more fully than in a publication list alone.

Collaborative Work
==================

My work depends on collaboration with experimental and computational
partners across RNA bioinformatics, structural biology, virology,
synthetic biology, and related areas. That includes close interaction
within my own :link-flat:`research group <{filename}/team.rst>`, but
also longer-standing collaborations with international partners whose
questions require a structure-aware computational perspective.

Some of the same expertise is also available in workshop or design-review format for groups that need focused external input on RNA structure, chemical probing interpretation, modelling, or computational design strategy. That work is described on the :link-flat:`services page </services>`.
