Rational Design of Mechanically Active RNAs
###########################################

:date: 2026-01-08
:modified: 2026-05-07
:tags: RNA design; xrRNA; synthetic biology
:category: publications
:slug: Rational-design-of-mechanically-active-RNAs
:author: mtw
:summary: A preprint-stage note on the design logic behind synthetic xrRNAs and mechanically active RNAs.
:title: A first look at rational design of mechanically active RNAs
:description: Preprint-stage overview of a mechanics-aware workflow for designing synthetic xrRNAs and probing how topology controls XRN1 resistance.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. frame:: Update

   This post was written when the manuscript first appeared as a
   preprint in January 2026. The peer-reviewed paper has since been
   accepted by *Nucleic Acids Research*. A separate post on the final
   published article will follow once the journal version is live in
   mid-May 2026.

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Walter-2026.001small.png
          :alt: Ring-like tertiary structure of a designed synthetic xrRNA
          :figclass: m-figure m-flat

Exoribonuclease-resistant RNAs (`xrRNAs`) are among the clearest
examples of mechanically active RNAs. Their function depends on a
ring-like topology that blocks 5' to 3' decay by enzymes such as XRN1.
That makes them attractive design targets, but also difficult ones,
because the relevant features are not captured well by conventional
secondary structure design alone.

The main interest of this work was whether that
kind of function could be approached rationally. The study starts from
topology rather than sequence conservation and asks which structural
elements are indispensable for XRN1 resistance. In the Aroa virus xrRNA
used as a benchmark, the two pseudoknots in the xrRNA do not contribute equally:
pseudoknot 2 behaves as the decisive gatekeeper of mechanical
resistance, whereas pseudoknot 1 is important but less determinant on
its own.

Those observations were then turned into a design workflow. Natural
mosquito-borne flavivirus xrRNAs were reduced to a symbolic
representation that preserves the three-way junction, the two
pseudoknots, and characteristic length constraints between structural
elements. Sequence generation was carried out with explicit structural
and topological constraints, followed by ensemble-based refinement,
SimRNA modelling, and molecular dynamics screening for ring closure and
directional force resistance. The point was not simply to inverse-fold a
target secondary structure, but to make topology part of the design
objective.

The synthetic constructs provide a useful progression. `syn-xrRNA1`
captured the general architecture `in silico` but remained too weak
experimentally. `syn-xrRNA2` strengthened the crucial topological region
and reached wild-type-like XRN1 resistance. `syn-xrRNA3` then removed
most of the familiar evolutionary sequence signal while preserving the
geometric and energetic requirements for function. Even in that reduced
form, the construct still folded into a bona fidae xrRNA architecture and
stalled XRN1 efficiently.

The main conceptual result of the preprint is the following:
mechanical RNA function could be approached through topology and
geometry without relying on obvious sequence ancestry. The broader
implications for synthetic biology and transcript engineering are
better discussed in the forthcoming publication post, once the
peer-reviewed paper is available in final form.

Citation
========

  | :link-flat-strong:`Rational design of mechanically active RNAs: de novo engineering of functional exoribonuclease-resistant RNAs <https://doi.org/10.1101/2026.01.08.698366>`
  | Jule Walter, Leonhard Sidl, Katrin Gutenbrunner, Denis Skibinski, Tim Kolberg, Ivo L. Hofacker, Hua-Ting Yao, Mario Mörl, :ul:`Michael T. Wolfinger`
  | *bioRxiv* 2026.01.08.698366 (2026) | :doi:`doi:10.1101/2026.01.08.698366 <https://doi.org/10.1101/2026.01.08.698366>` | :link-flat:`Preprint PDF <{static}/files/papers/Walter-2026__PREPRINT.pdf>`
