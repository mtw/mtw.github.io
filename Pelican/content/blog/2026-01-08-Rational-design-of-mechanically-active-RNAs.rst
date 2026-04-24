Rational Design of Mechanically Active RNAs
###########################################

:date: 2026-01-08
:modified: 2026-04-24
:tags: RNA design; xrRNA; synthetic biology
:category: publications
:slug: Rational-design-of-mechanically-active-RNAs
:author: mtw
:summary: A mechanics-aware RNA design workflow identifies topological design rules for xrRNAs and produces fully synthetic exoribonuclease-resistant RNAs with wild-type-like XRN1 resistance.
:title: Rational design of mechanically active RNAs and synthetic xrRNAs
:description: De novo engineering of functional xrRNAs using symbolic design constraints, molecular dynamics-guided selection, and experimental XRN1 validation.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Walter-2026.001small.png
          :alt: Ring-like tertiary structure of a designed synthetic xrRNA
          :figclass: m-figure m-flat

Exoribonuclease-resistant RNAs (xrRNAs) are among the clearest examples of mechanically active RNAs. Their function does not come from binding a ligand or catalyzing a reaction, but from adopting a ring-like topology that physically blocks 5' to 3' degradation by enzymes such as XRN1. That makes them conceptually attractive design targets, but also unusually difficult ones: the relevant features involve pseudoknots, base triples, and a threaded topology that conventional RNA design methods do not capture well.

This paper asks whether that kind of mechanical function can be designed on purpose. Instead of starting from sequence conservation, the study starts from topology. Using the mosquito-borne Aroa virus xrRNA as a benchmark, we first perturbed the two pseudoknots that stabilize the ring-like fold and measured how strongly each perturbation affects XRN1 stalling. The key result is that pseudoknot 2 acts as the primary gatekeeper of mechanical resistance: weakening it reduces protection, and deleting it abolishes resistance altogether. Pseudoknot 1 still matters, but more as a stabilizing contributor than as the decisive topological switch.

Those mechanistic insights were then translated into a design framework. Natural mosquito-borne flavivirus xrRNAs were summarized as a symbolic model that preserves the three-way junction, the two pseudoknots, and the observed length correlations between structural elements. Sequence generation was carried out with the `Infrared <https://github.com/s-will/Infrared>`_ framework under explicit structural and topological constraints, followed by ensemble-based refinement, SimRNA 3D modeling, and molecular-dynamics screening for ring closure and directional force resistance. In other words, this is not just inverse folding for a secondary structure target. It is a closed design loop in which topology and mechanical behavior are part of the objective.

The progression through the three synthetic constructs is especially instructive. The first design, `syn-xrRNA1`, formed the expected ring-like fold in silico but remained too weak in vitro, consistent with incomplete pseudoknot formation. After strengthening pseudoknot 2 and improving the linker geometry, `syn-xrRNA2` reached wild-type-like XRN1 resistance. The final construct, `syn-xrRNA3`, goes one step further: most evolutionary sequence information was removed, leaving only the topological and energetic requirements needed for function. Even so, the RNA still folded into the threaded xrRNA architecture, stalled XRN1 efficiently, and showed simulated unfolding forces above the natural reference.

That last point is the conceptual center of the paper. `syn-xrRNA3` behaves like a functional xrRNA, yet it falls into the random-sequence range when evaluated with covariance models trained on known mosquito-borne flavivirus xrRNAs. In other words, the design escapes homology detection while preserving mechanical function. This is strong evidence that xrRNA activity can be specified through topology and geometry rather than through recognizable sequence ancestry.

From an RNA design perspective, this is a meaningful shift. It shows that mechanically defined RNA function can be engineered rationally without relying on large multiple-sequence alignments, high-throughput selection, or strong sequence conservation. That opens interesting directions for synthetic biology and RNA therapeutics, where one may want to tune transcript stability or protect selected regions from exonucleolytic decay without inserting native viral sequences. More broadly, the work turns xrRNAs from an elegant virology story into a practical design problem, and provides a concrete framework for building mechanically active RNAs on purpose.

.. frame:: Abstract

   Mechanically active RNAs represent an emerging class of biomolecules whose function derives from resisting molecular forces. Among them, exoribonuclease-resistant RNAs (xrRNAs) achieve this by folding into a ring-like topology that physically blocks 5’ → 3’ degradation. However, despite years of structural insight, the rational design of such mechanically functional RNA devices has remained elusive. Here, we describe a mechanics-aware RNA design approach that enables de novo engineering of functional xrRNAs. We first identify structural determinants of force resistance by perturbing pseudoknot architecture in a model xrRNA and quantifying resulting efficiencies in the stalling of exoribonuclease XRN1. We then implement these rules in a design framework that integrates explicit topological constraints with molecular dynamics-guided optimization. The resulting synthetic xrRNAs reproduce the ring-like architecture and stall exoribonuclease XRN1 with wild-type-like efficiency. Our top-performing constructs exhibit minimal sequence similarity to known xrRNAs and evade detection by covariance models, yet remain fully functional in vitro. Together, our results show that mechanical function can be rationally designed independent of evolutionary ancestry, laying the groundwork for the design of RNA elements that modulate decay and fine-tune the mechanical stability of engineered transcripts.

Citation
========

  | :link-flat-strong:`Rational design of mechanically active RNAs: de novo engineering of functional exoribonuclease-resistant RNAs <{filename}/blog/2026-01-08-Rational-design-of-mechanically-active-RNAs.rst>`
  | Jule Walter, Leonhard Sidl, Katrin Gutenbrunner, Denis Skibinski, Tim Kolberg, Ivo L. Hofacker, Hua-Ting Yao, Mario Mörl, :ul:`Michael T. Wolfinger`
  | *Nucleic Acids Res.* accepted (2026) | :doi:`doi:10.64898/2026.01.08.698366 <https://doi.org/10.64898/2026.01.08.698366>` | :link-flat:`Preprint PDF <{static}/files/papers/Walter-2026__PREPRINT.pdf>`
