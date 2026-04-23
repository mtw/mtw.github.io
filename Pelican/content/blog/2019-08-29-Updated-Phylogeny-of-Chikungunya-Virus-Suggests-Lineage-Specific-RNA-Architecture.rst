Updated Phylogeny of Chikungunya Virus Suggests Lineage-Specific RNA Architecture
#################################################################################

:date: 2019-08-29
:modified: 2024-10-10
:tags: molecular epidemiology; virus bioinformatics; alphavirus; virology
:category: publications
:slug: Updated-Phylogeny-of-Chikungunya-Virus-Suggests-Lineage-Specific-RNA-Architecture
:author: mtw
:title: Chikungunya virus phylogeny and lineage-specific RNA structures
:description: Our study finds multiple independent clades in the ECSA lineage of Chikungunya virus and uncovers evidence of lineage-specific RNA structure conservation.
:summary: An updated CHIKV phylogeny based on 598 genomes, linking lineage structure to conserved and lineage-specific 3' UTR RNA architectures.

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.001.png
          :alt: Updated phylogeny and lineage structure of Chikungunya virus
          :figclass: m-figure m-flat

Chikungunya virus (CHIKV) is usually discussed in terms of a small set of named geographic lineages, but that picture has become increasingly inadequate as more genome sequences have accumulated. In this study we revisited CHIKV evolution using 598 complete genomes and asked two connected questions: how well the traditional lineage labels still reflect the phylogeny, and whether the distinct clades also differ in the organization of their untranslated regions.

The phylogenetic analysis was based on the two viral open reading frames and used a maximum-likelihood framework with explicit support assessment. One of the central results is that the historically defined ECSA group is not best understood as a single lineage. Instead, the data support several African sublineages with different evolutionary histories, including Eastern, Middle, and Southern African components. That distinction matters because the major epidemic clades outside Africa can be traced back to different parts of this broader African diversity. In the revised view used in the paper, the Indian Ocean lineage derives from Eastern African ancestors, while the South American outbreak strain is linked to Middle African taxa.

The second part of the paper focuses on the CHIKV 3' UTR, a region known to carry repeated sequence elements but whose structural organization had remained unclear. Using comparative RNA analysis, covariance-model based homology searches, and consensus secondary-structure prediction, we found that the repeat-rich 3' UTR is not just a collection of duplicated sequence blocks. Instead, it follows an alternating architecture of conserved structured and unstructured elements. The structured part consists of stem-loop elements termed SL-a and SL-b, a Y-shaped element SL-Y, and a conserved sequence element near the terminus, while the intervening repeat regions remain predominantly unpaired.

This structured-versus-unstructured organization is one of the more interesting aspects of the study. The unstructured repeat regions are unlikely to be mere spacers. Because they remain accessible, they may act as structural insulators between neighboring RNA elements or provide binding surfaces for host proteins. The paper points in particular to repeated `UAG` motifs in these accessible regions, which makes interactions with proteins such as Musashi plausible, although that remains a functional hypothesis rather than a demonstrated mechanism.

Another useful outcome is that the 3' UTR architectures differ systematically between lineages. Some elements are shared across essentially all CHIKV groups, while others vary in copy number or arrangement, and recent American isolates of the Asian Urban lineage show evidence of partial duplication events. This suggests that CHIKV evolution in the 3' UTR is not just sequence drift. Rather, the virus appears to rearrange modular RNA building blocks while preserving an overall architectural pattern. That is a more informative model than treating the repeat region as a simple low-complexity tail.

From a computational RNA perspective, this paper is also a good example of what comparative genomics can do even when strong covariation support is limited. CHIKV 3' UTR sequences are often too similar, and the available sampling is too outbreak-biased, to expect the kind of covariation signal seen in deeply diverged structured RNAs. Even so, combining phylogeny, repeated architecture, local thermodynamic stability, and homology modeling is enough to identify plausible conserved RNA elements and to formulate experimentally testable hypotheses about their role in replication, host adaptation, and lineage-specific biology.


.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. raw:: html

  <object data="{static}/files/papers/deBernardiSchneider-2019b.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/deBernardiSchneider-2019b.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>


.. frame:: Abstract

   Chikungunya virus (CHIKV), a mosquito-borne alphavirus of the family Togaviridae, has recently emerged in the Americas from lineages from two continents: Asia and Africa. Historically, CHIKV circulated as at least four lineages worldwide with both enzootic and epidemic transmission cycles. To understand the recent patterns of emergence and the current status of the CHIKV spread, updated analyses of the viral genetic data and metadata are needed. Here, we performed phylogenetic and comparative genomics screens of CHIKV genomes, taking advantage of the public availability of many recently sequenced isolates. Based on these new data and analyses, we derive a revised phylogeny from nucleotide sequences in coding regions. Using this phylogeny, we uncover the presence of several distinct lineages in Africa that were previously considered a single one. In parallel, we performed thermodynamic modeling of CHIKV untranslated regions (UTRs), which revealed evolutionarily conserved structured and unstructured RNA elements in the 3’UTR. We provide evidence for duplication events in recently emerged American isolates of the Asian CHIKV lineage and propose the existence of a flexible 3’UTR architecture among different CHIKV lineages.


Figures and Data
================

.. image-grid::

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.001.png

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.002.png
  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.003.png

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.004.png
  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.005.png

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.006.png
  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b/QuickSlide__deBernardiSchneider-2019b.007.png

Citation
========

  | :link-flat-strong:`Updated Phylogeny of Chikungunya Virus Suggests Lineage-Specific RNA Architecture <{filename}/blog/2019-08-29-Updated-Phylogeny-of-Chikungunya-Virus-Suggests-Lineage-Specific-RNA-Architecture.rst>`
  | Adriano de Bernardi Schneider, Roman Ochsenreiter, Reilly Hostager, Ivo L. Hofacker, Daniel Janies, :ul:`Michael T. Wolfinger`
  | *Viruses* 11:798 (2019) | :doi:`doi:10.3390/v11090798 <https://doi.org/10.3390/v11090798>` | :link-flat:`PDF <{static}/files/papers/deBernardiSchneider-2019b.pdf>` | :link-flat:`Figures <{static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019b.pdf>`


See Also
========

  | :link-flat-strong:`Dynamic Molecular Epidemiology Reveals Lineage-Associated Single-Nucleotide Variants That Alter RNA Structure in Chikungunya Virus  <{filename}/blog/2021-02-08-Dynamic_Molecular_Epidemiology_Reveals_Lineage-Associated_Single-Nucleotide_Variants_That_Alter_RNA_Structure_in_Chikungunya_Virus.rst>`
  | Thomas Spicher, Markus Delitz, Adriano de Bernardi Schneider, :ul:`Michael T. Wolfinger`
  | *Genes* 12 (2):239 (2021) | :doi:`doi:10.3390/genes12020239 <https://doi.org/10.3390/genes12020239>` | :link-flat:`PDF <{static}/files/papers/Spicher-2021.pdf>` | :link-flat:`Figures <{static}/files/QuickSlide/QuickSlide__Spicher-2021.pdf>` 
