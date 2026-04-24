In Silico Design of Ligand Triggered RNA Switches
#################################################

:date: 2018-07-01
:modified: 2026-04-23
:tags: energy landscapes; new method; RNA folding kinetics; RNA design; ViennaRNA; synthetic biology; co-transcriptional RNA folding
:category: publications
:slug: In-Silico-Design-of-Ligand-Triggered-RNA-Switches
:author: mtw
:summary: A computational workflow for designing ligand-triggered RNA switches, with emphasis on sequence design, folding kinetics, and candidate prioritization.
:title: In silico design of ligand-triggered RNA switches
:description: Designing ligand-triggered riboswitches: Computational workflow and in silico analysis for studying the RNA folding kinetics of rationally designed sequences

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Designing a useful ligand-triggered RNA switch is not just a matter of finding a sequence that can fold into two states. The real problem is to engineer a sequence whose relevant conformations, ligand competence, and switching kinetics are all compatible with the intended mechanism.

This work lays out a concrete in silico workflow for that problem. It starts from a well-characterized aptamer, exemplified here with the theophylline aptamer, and treats ligand binding as one structurally defined state of the switch. The design task then becomes one of balancing that binding-competent conformation against an alternative fold that disrupts it in the absence of ligand.

One useful contribution of the paper is that it makes the objective function explicit. Instead of treating switch design as a vague search for "good" sequences, the workflow defines quantitative criteria for what the sequence should do. That matters because RNA design tends to fail when the desired mechanism is underspecified. If the design objective does not encode the structural logic of the switch, ranking candidate sequences becomes little more than guesswork.

The other key point is kinetics. For many RNA design problems, equilibrium structure alone is not enough. A candidate may satisfy static structural constraints and still perform poorly if the switching pathway is too slow, too indirect, or dominated by off-target intermediates. That is why the workflow includes an analysis of folding kinetics rather than stopping at secondary-structure prediction.

The result is a design pipeline that helps filter and rank candidate sequences before any experimental work begins. It does not guarantee that a proposed switch will function in a cellular context, and it does not replace experimental validation. What it does offer is a principled way to reduce the search space and focus attention on sequences whose structures and dynamic behavior are at least consistent with the intended design.

For computational RNA biology, that is the real value of this kind of work. It turns riboswitch design from an intuition-led exercise into an optimization problem with explicit structural and kinetic criteria. That framing also makes the workflow adaptable: once the design assumptions are clear, the same logic can be extended to other aptamers, other switching scenarios, and more elaborate regulatory mechanisms.

If you are evaluating an RNA switch, riboswitch, or structure-aware design workflow, I also offer independent design reviews for research teams and biotech groups through my :link-flat:`services page <{filename}/services.rst>`.

.. raw:: html

  <object data="{static}/files/papers/Findeiss-2018__PREPRINT.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Findeiss-2018__PREPRINT.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

  This contribution sketches a work flow to design an RNA switch that is able to adapt two structural conformations in a ligand-dependent way. A well characterized RNA aptamer, i.e., knowing its Kd and adaptive structural features, is an essential ingredient of the described design process. We exemplify the principles using the well-known theophylline aptamer throughout this work. The aptamer in its ligand-binding competent structure represents one structural conformation of the switch while an alternative fold that disrupts the binding-competent structure forms the other conformation. To keep it simple we do not incorporate any regulatory mechanism to control transcription or translation. We elucidate a commonly used design process by explicitly dissecting and explaining the necessary steps in detail. We developed a novel objective function which specifies the mechanistics of this simple, ligand-triggered riboswitch and describe an extensive in silico analysis pipeline to evaluate important kinetic properties of the designed sequences. This protocol and the developed software can be easily extended or adapted to fit novel design scenarios and thus can serve as a template for future needs.

Citation
========

  | :link-flat-strong:`In silico design of ligand triggered RNA switches <https://doi.org/10.1016/j.ymeth.2018.04.003>`
  | Sven Findeiß, Stefan Hammer, Michael T. Wolfinger, Felix Kühnl, Christoph Flamm, Ivo L.Hofacker
  | *Methods* 143:90-101 (2018) | :doi:`doi: 10.1016/j.ymeth.2018.04.003 <https://doi.org/10.1016/j.ymeth.2018.04.003>` | :link-flat:`Preprint PDF <{static}/files/papers/Findeiss-2018__PREPRINT.pdf>`
