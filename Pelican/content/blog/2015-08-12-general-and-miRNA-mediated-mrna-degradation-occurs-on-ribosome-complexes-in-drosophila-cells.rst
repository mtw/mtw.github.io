General and miRNA-mediated mRNA degradation occurs on ribosome complexes in Drosophila cells
############################################################################################

:date: 2015-08-12
:modified: 2026-04-24
:tags: NGS
:category: publications
:slug: general-and-miRNA-mediated-mrna-degradation-occurs-on-ribosome-complexes-in-drosophila-cells
:author: mtw
:summary: This study shows that bulk and miRNA-guided mRNA degradation in Drosophila cells occurs on ribosome-associated messenger ribonucleoprotein complexes, linking decay machinery, translation, and high-throughput sequencing of decapped intermediates.
:title: mRNA degradation occurs on ribosome complexes in Drosophila cells
:description: A Drosophila study combining ribosome purification, decay-factor profiling, and sequencing of decapped intermediates to show that mRNA degradation is tightly coupled to ribosome-associated complexes.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Antic-2015.001small.webp
          :alt: Workflow for sequencing decapped mRNA intermediates and summary of their abundance on ribosome complexes versus whole-cell lysate
          :figclass: m-figure m-flat

This paper sits in a different part of my publication list than the RNA structure and folding work, but in hindsight it connects to it more than it may seem at first glance. Before I started to investigate viral xrRNAs and the ways in which structured RNAs can resist exonucleolytic decay, I was interested in a more general question: where does 5' to 3' mRNA degradation actually take place in the cell, and how tightly is it coupled to translation?

At the time, the coupling between translation and mRNA turnover was already widely appreciated, but the physical location of that coupling was still not entirely clear. One could imagine a handoff model in which translating ribosomes and decay machineries act in sequence, or a more direct model in which degrading mRNAs remain associated with ribosome-containing complexes during turnover. This study addressed that distinction experimentally in *Drosophila* cells and asked whether the same picture also applies to miRNA-mediated decay.

The approach combined several complementary readouts. Polysome profiling and ribosome affinity purification were used to isolate ribosome-associated complexes. These preparations were then probed for canonical translation factors, general deadenylation and decapping components, and key miRNA pathway proteins such as AGO1 and GW182. The crucial control was that these associations depended on intact RNA, arguing that the decay factors were not simply sticking nonspecifically to ribosomal proteins but were traveling with messenger ribonucleoprotein complexes engaged with mRNA.

The most informative part of the paper, in my view, is the sequencing-based analysis of decapped degradation intermediates. The workflow captured 5' monophosphorylated mRNA fragments from ribosome complexes and compared them with corresponding fragments from whole-cell lysate. That moved the study beyond a few marker transcripts or individual immunoblots. Instead, it asked the question transcriptome-wide: are decapped intermediates generally depleted from ribosome-associated fractions, or do they remain there at similar relative abundance?

The answer was strikingly broad. Roughly 93% of the detected decapped fragments were present at essentially the same relative abundance in ribosome complexes as in the total lysate. That is a strong argument against the idea that decapping is followed by rapid physical separation from translational assemblies for most transcripts. Rather, the data support a model in which bulk 5' to 3' decay commonly proceeds on ribosome-associated mRNPs, with miRNA-mediated decay fitting into the same overall framework rather than constituting a fully separate compartmentalized process.

That result matters biologically because it shifts the emphasis from static cellular compartments to dynamic functional coupling. It suggests that translation, deadenylation, decapping, and exonucleolytic degradation should often be understood as parts of the same continuum of messenger RNA handling. For miRNA biology this was especially relevant: AGO1 and GW182 were not just abstract regulatory labels but factors connected to ribosome-associated decay states of target RNAs.

Seen from later work on xrRNAs, this paper also sharpened the next question. If much of 5' to 3' decay is happening on ribosome-associated messenger complexes, then structured RNA elements that can impede exonucleases become even more interesting, because they do not act in an isolated degradation chamber. They act in the middle of an already crowded and highly coordinated post-transcriptional environment. In that sense, this study predates the xrRNA projects but helped define the decay-centered perspective from which those later questions became compelling.

So although this is not an RNA structure paper, it is an important mechanistic one. It combines classical biochemical fractionation with a transcriptome-wide sequencing readout to make a fairly clean point: in *Drosophila* cells, both general and miRNA-mediated mRNA degradation are closely tied to ribosome-associated complexes. For anyone interested in how gene expression is controlled after transcription, that is a useful result to keep in mind.

.. frame:: Abstract

  The translation and degradation of mRNAs are two key steps in gene
  expression that are highly regulated and targeted by many factors,
  including microRNAs (miRNAs). While it is well established that translation
  and mRNA degradation are tightly coupled, it is still not entirely clear
  where in the cell mRNA degradation takes place. In this study, we
  investigated the possibility of mRNA degradation on the ribosome in
  Drosophila cells. Using polysome profiles and ribosome affinity
  purification, we could demonstrate the copurification of various
  deadenylation and decapping factors with ribosome complexes. Also, AGO1 and
  GW182, two key factors in the miRNA-mediated mRNA degradation pathway, were
  associated with ribosome complexes. Their copurification was dependent on
  intact mRNAs, suggesting the association of these factors with the mRNA
  rather than the ribosome itself. Furthermore, we isolated decapped mRNA
  degradation intermediates from ribosome complexes and performed
  high-throughput sequencing analysis. Interestingly, 93% of the decapped
  mRNA fragments (approximately 12,000) could be detected at the same
  relative abundance on ribosome complexes and in cell lysates. In summary,
  our findings strongly indicate the association of the majority of bulk
  mRNAs as well as mRNAs targeted by miRNAs with the ribosome during their
  degradation.

Citation
========

  | :link-flat-strong:`General and miRNA-mediated mRNA degradation occurs on ribosome complexes in Drosophila cells <http://mcb.asm.org/content/35/13/2309>`
  | Sanja Antic, Michael T. Wolfinger, Anna Skucha, Stefanie Hosiner and Silke Dorner
  | *Mol. Cell. Biol.* 35(13), 2309-2320 (2015) | :doi:`doi:10.1128/MCB.01346-14 <https://doi.org/10.1128/MCB.01346-14>` | :link-flat:`PDF <{static}/files/papers/Antic-2015.pdf>`
