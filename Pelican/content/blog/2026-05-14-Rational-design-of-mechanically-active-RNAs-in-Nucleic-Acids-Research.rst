Rational Design of Mechanically Active RNAs in Nucleic Acids Research
#####################################################################

:date: 2026-05-14
:modified: 2026-05-07
:tags: RNA design; xrRNA; synthetic biology
:category: publications
:slug: Rational-design-of-mechanically-active-RNAs-in-Nucleic-Acids-Research
:author: mtw
:summary: The peer-reviewed NAR paper shows that synthetic xrRNAs can be designed from topological rules and validated experimentally as mechanically active RNAs.
:title: Published in NAR: rational design of mechanically active RNAs
:description: Final publication post for the Nucleic Acids Research paper on synthetic xrRNAs, topological RNA design, and experimentally validated mechanical resistance.
:status: skip

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

This paper marks the transition of the `xrRNA` story from comparative
RNA virology into deliberate RNA engineering. Exoribonuclease-resistant
RNAs have been known for years as structured viral elements that stall
5' to 3' decay through a threaded, mechanically resistant fold. The
question addressed here is whether that function can be designed on
purpose, rather than merely described in natural systems.

The answer is yes, but only if topology is treated as part of the
design problem from the start. The paper identifies which structural
features matter most for XRN1 resistance, translates those observations
into an explicit symbolic design model, and then uses that model to
generate synthetic candidates that are screened computationally and
validated experimentally. The workflow combines structural constraints,
ensemble-based filtering, 3D modelling, and molecular-dynamics
selection for ring closure and directional force resistance.

One of the clearest mechanistic results concerns the two pseudoknots
that stabilize the xrRNA fold. They do not contribute symmetrically.
Pseudoknot 2 is the decisive gatekeeper of mechanical resistance, while
pseudoknot 1 acts more as a supporting stabilizer. That distinction is
important because it turns a structural motif into a tractable design
rule.

The three synthetic constructs illustrate how the design space was
worked through. `syn-xrRNA1` approached the right topology but remained
too weak in vitro. `syn-xrRNA2` improved the critical pseudoknot and
linker geometry and reached wild-type-like XRN1 resistance. `syn-xrRNA3`
goes furthest: most familiar sequence signal is removed, yet the RNA
still folds into a functional threaded architecture and resists XRN1
efficiently. In other words, the construct preserves mechanical
function without preserving recognizable evolutionary ancestry.

That is the broader significance of the paper. It shows that one can
design mechanically active RNA elements by preserving topology and
geometric constraints rather than copying a natural viral sequence. For
synthetic biology and therapeutic RNA engineering, that opens the
possibility of tuning decay resistance and transcript stability without
importing long native viral elements wholesale.

This publication also closes a loop with earlier work on natural xrRNAs
and structured viral RNAs. Comparative analysis established what these
elements look like in nature. The present paper asks what remains of
that function once the sequence history is stripped away and only the
topological logic is kept. That shift from description to design is
what makes the paper especially satisfying.

.. frame:: Publication Note

   This post is prepared for the final journal publication of the paper
   in *Nucleic Acids Research*. When the article goes live, the formal
   citation, DOI, and PDF link should be updated here and the
   corresponding entry in ``publications.rst`` should be redirected from
   the January preprint note to this page.

Citation
========

  | :link-flat-strong:`Rational design of mechanically active RNAs: de novo engineering of functional exoribonuclease-resistant RNAs <{filename}/blog/2026-05-14-Rational-design-of-mechanically-active-RNAs-in-Nucleic-Acids-Research.rst>`
  | Jule Walter, Leonhard Sidl, Katrin Gutenbrunner, Denis Skibinski, Tim Kolberg, Ivo L. Hofacker, Hua-Ting Yao, Mario Mörl, :ul:`Michael T. Wolfinger`
  | *Nucleic Acids Res.* (2026) | final DOI and PDF link to be added when the journal version is live
