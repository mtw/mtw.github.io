Rational Design of Mechanically Active RNAs
###########################################

:date: 2026-05-12
:modified: 2026-05-12
:tags: RNA design; xrRNA; synthetic biology
:category: publications
:slug: Rational-design-of-mechanically-active-RNAs-in-Nucleic-Acids-Research
:author: mtw
:summary: This Nucleic Acids Research paper shows that synthetic xrRNAs can be designed from topological rules and validated experimentally as mechanically active RNAs.
:title: Rational design of mechanically active RNAs
:description: Nucleic Acids Research paper on synthetic xrRNAs, topological RNA design, and experimentally validated mechanical resistance.

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

This paper extends the `xrRNA` story from comparative RNA virology into
explicit RNA engineering. Exoribonuclease-resistant RNAs are structured
viral elements that stall 5' to 3' decay through a threaded,
mechanically resistant fold. The question addressed here is whether
that function can be specified de novo rather than inferred from a
natural sequence that already carries it.

The paper treats topology as part of the design objective from the
start. Structural features relevant to XRN1 resistance are reduced to
an explicit symbolic model, which is then used to generate synthetic
candidates that are filtered computationally and tested
experimentally. The workflow combines structural constraints,
ensemble-based screening, three-dimensional modelling, and
molecular-dynamics selection for ring closure and directional force
resistance.

One of the clearest mechanistic results concerns the two pseudoknots
that stabilize the xrRNA fold. They do not contribute symmetrically.
Pseudoknot 2 is the decisive gatekeeper of mechanical resistance, while
pseudoknot 1 acts more as a supporting stabilizer. That distinction is
important because it turns a structural motif into a tractable design
rule.

The three synthetic constructs show how the design space was narrowed.
`syn-xrRNA1` approaches the intended topology but remains too weak
in vitro. `syn-xrRNA2` improves the critical pseudoknot and linker
geometry and reaches wild-type-like XRN1 resistance. `syn-xrRNA3`
goes further: familiar sequence signal is largely removed, yet the RNA
still folds into a functional threaded architecture and resists XRN1
efficiently.

To my knowledge, this is the first example of a fully de novo designed
RNA in which a complex mechanically active fold has been specified from
topological rules and then validated experimentally. That makes the
paper a genuine breakthrough. It shows that mechanically active RNA
elements can be designed by preserving topology and geometric
constraints rather than by copying a natural viral sequence. For
synthetic biology and therapeutic RNA engineering, this opens the
possibility of tuning decay resistance and transcript stability without
importing long native viral elements wholesale.

This publication also closes a loop with earlier work on natural xrRNAs
and structured viral RNAs. Comparative analysis established the
relevant folds in nature. The present paper asks which parts of that
function survive once sequence history is stripped away and only the
topological logic is retained.

The earlier comparative side of that story runs through
:link-flat:`Discoveries of Exoribonuclease-Resistant Structures of Insect-Specific Flaviviruses Isolated in Zambia <{filename}/blog/2020-09-14-Discoveries-of-Exoribonuclease-Resistant-Structures-of-Insect-Specific-Flaviviruses-Isolated-in-Zambia.rst>`,
:link-flat:`Mpulungu virus and unique xrRNAs in a novel African tick flavivirus <{filename}/blog/2021-03-01-An_African_Tick_Flavivirus_Forming_an_Independent_Clade_Exhibits_Unique_Exoribonuclease-Resistant_RNA_Structures_in_the_Genomic_three_prime-Untranslated_Region.rst>`,
and :link-flat:`Strukturierte RNAs in Viren <{filename}/blog/2023-03-23-Strukturierte-RNAs-in-Viren.rst>`.
The January :link-flat:`preprint-stage note <{filename}/blog/2026-01-08-Rational-design-of-mechanically-active-RNAs.rst>` remains online as a shorter record of how the project was framed before peer-reviewed publication.

Citation
========

  | :link-flat-strong:`Rational design of mechanically active RNAs: de novo engineering of functional exoribonuclease-resistant RNAs <https://academic.oup.com/nar/article/54/9/gkag473/8676204>`
  | Jule Walter, Leonhard Sidl, Katrin Gutenbrunner, Denis Skibinski, Tim Kolberg, Ivo L. Hofacker, Hua-Ting Yao, Mario Mörl, :ul:`Michael T. Wolfinger`
  | *Nucleic Acids Res.* 54(9):gkag473 (2026) | :doi:`doi:10.1093/nar/gkag473 <https://doi.org/10.1093/nar/gkag473>` | :link-flat:`Article <https://academic.oup.com/nar/article/54/9/gkag473/8676204>` | :link-flat:`PDF <{static}/files/papers/Walter-2026.pdf>`
