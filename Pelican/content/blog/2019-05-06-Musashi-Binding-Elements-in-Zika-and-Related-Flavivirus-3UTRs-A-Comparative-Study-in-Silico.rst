Musashi Binding Elements in Zika Virus 3'UTR
############################################

:date: 2019-05-06
:modified: 2023-04-09
:tags: non-coding RNA; virus bioinformatics; ViennaRNA; RNA-Protein interaction; flavivirus
:category: publications
:slug: Musashi-Binding-Elements-in-Zika-and-Related-Flavivirus-3UTRs-A-Comparative-Study-in-Silico
:author: mtw
:summary: A comparative analysis of Musashi binding element accessibility in Zika virus and related flavivirus 3' UTRs using thermodynamic RNA structure modeling.
:description: Comparative thermodynamic analysis of Musashi binding elements in flavivirus 3' UTRs, with a focus on accessibility in Zika virus.
:title: Musashi binding elements in Zika virus 3'UTR



.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a/QuickSlide__deBernardiSchneider-2019a.002.png
          :alt: Accessibility of Musashi binding elements in Zika virus and related flaviviruses
          :figclass: m-figure m-flat

Musashi-1 is an RNA-binding protein that is highly expressed in neural stem and progenitor cells, and earlier experimental work had suggested that it can bind the Zika virus 3' UTR and enhance viral replication. That makes the structural context of Musashi binding elements in viral RNA immediately relevant: binding depends not just on the presence of a `UAG` core motif, but on whether that motif is exposed in a single-stranded region that is accessible to the protein.

This paper addresses exactly that question with a thermodynamic RNA-structure model. We screened curated flavivirus 3' UTRs for `UAG` motifs and evaluated how accessible each site is in its native sequence context. Rather than just folding a single minimum-free-energy structure, the analysis uses opening energies derived from ensemble calculations in sliding windows and compares them to dinucleotide-shuffled sequence controls. The resulting z scores make it possible to ask whether a given Musashi binding element is unusually exposed relative to what would be expected from local sequence composition alone.

For Zika virus, the result is clear. In both the African and the Asian/American lineages, `UAG` belongs to the most accessible trinucleotides in the 3' UTR, and the surrounding pentanucleotide context remains accessible as well. The Asian/American lineage is especially striking: in the Brazilian isolate used here, all `UAG` motifs in the 3' UTR show negative opening-energy z scores, meaning that they are consistently predicted to occur in unpaired structural contexts. That fits well with the idea that Musashi binding is structurally favored in epidemic ZIKV strains.

The comparative part of the study is just as important. The same calculation was carried out across mosquito-borne, tick-borne, insect-specific, and no-known-vector flaviviruses. ZIKV from the Asian/American lineage ranked as the most Musashi-accessible among the mosquito-borne flaviviruses in the dataset, but it was not the only virus with accessible Musashi motifs. Some West Nile, yellow fever, Powassan, Karshi, and insect-specific flaviviruses also contain strongly accessible `UAG` sites. That does not mean that all of these viruses share the same neuropathology as ZIKV, but it does show that ZIKV is not uniquely equipped with Musashi-compatible RNA motifs.

Another useful result is that Musashi binding elements are not randomly scattered across flavivirus 3' UTRs. By mapping the motifs onto conserved structural elements, the study found that dumbbell elements in particular often carry two conserved `UAG` motifs in a shared structural context. That is interesting because dumbbell RNAs are already known as functionally important 3' UTR elements in many flaviviruses. The combination of structural conservation and repeated Musashi-compatible motifs suggests that these sites are worth testing experimentally rather than treating them as incidental sequence matches.

Conceptually, this work is less about proving a single mechanism and more about building a tractable computational screen for host-factor compatibility in viral RNAs. Accessibility alone is not enough to predict congenital infection or neurotropism, and the paper is careful not to claim that it is. But opening-energy calculations do provide a useful way to prioritize candidate binding sites and candidate viruses for follow-up experiments. In that sense, the study connects RNA secondary-structure thermodynamics with a concrete virological question: which flaviviruses place Musashi binding motifs in structural contexts that are likely to matter biologically?

.. frame:: Abstract

  Zika virus (ZIKV) belongs to a class of neurotropic viruses that have the ability to cause congenital infection, which can result in microcephaly or fetal demise. Recently, the RNA-binding protein Musashi-1 (Msi1), which mediates the maintenance and self-renewal of stem cells and acts as a translational regulator, has been associated with promoting ZIKV replication, neurotropism, and pathology. Msi1 predominantly binds to single-stranded motifs in the 3′ untranslated region (UTR) of RNA that contain a UAG trinucleotide in their core. We systematically analyzed the properties of Musashi binding elements (MBEs) in the 3′UTR of flaviviruses with a thermodynamic model for RNA folding. Our results indicate that MBEs in ZIKV 3′UTRs occur predominantly in unpaired, single-stranded structural context, thus corroborating experimental observations by a biophysical model of RNA structure formation. Statistical analysis and comparison with related viruses show that ZIKV MBEs are maximally accessible among mosquito-borne flaviviruses. Our study addresses the broader question of whether other emerging arboviruses can cause similar neurotropic effects through the same mechanism in the developing fetus by establishing a link between the biophysical properties of viral RNA and teratogenicity. Moreover, our thermodynamic model can explain recent experimental findings and predict the Msi1-related neurotropic potential of other viruses.

Figures and Data
================

.. image-grid::

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a/QuickSlide__deBernardiSchneider-2019a.001.png

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a/QuickSlide__deBernardiSchneider-2019a.002.png
  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a/QuickSlide__deBernardiSchneider-2019a.003.png

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a/QuickSlide__deBernardiSchneider-2019a.004.png
  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a/QuickSlide__deBernardiSchneider-2019a.005.png

  {static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a/QuickSlide__deBernardiSchneider-2019a.006.png


Citation
========

  | :link-flat-strong:`Musashi Binding Elements in Zika and Related Flavivirus 3’UTRs: A Comparative Study in Silico <https://doi.org/10.1038/s41598-019-43390-5>`
  | Adriano de Bernardi Schneider, :ul:`Michael T. Wolfinger`
  | *Sci. Rep.* 9(1):6911 (2019) | :doi:`doi:10.1038/s41598-019-43390-5 <https://doi.org/10.1038/s41598-019-43390-5>` | :link-flat:`PDF <{static}/files/papers/deBernardiSchneider-2019a.pdf>` | :link-flat:`Figures <{static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a.pdf>`


See Also
========

  | :link-flat-strong:`Theoretical studies on RNA recognition by Musashi 1 RNA–binding protein <{filename}/blog/2022-07-26-Theoretical-studies-on-RNA-recognition-by-Musashi1-RNA-binding-protein.rst>`
  | Nitchakan Darai, Panupong Mahalapbutr, Peter Wolschann, Vannajan Sanghiran Lee, :ul:`Michael T. Wolﬁnger`, Thanyada Rungrotmongkol
  | *Sci. Rep.* 12:12137 (2022) | :doi:`doi:10.1038/s41598-022-16252-w <https://doi.org/10.1038/s41598-022-16252-w>` | :link-flat:`PDF <{static}/files/papers/Darai-2022.pdf>` | :link-flat:`Figures <{static}/files/QuickSlide/QuickSlide__Darai-2022.pdf>`

  | :link-flat-strong:`A Structural Refinement Technique for Protein-RNA Complexes Using a Combination of AI-based Modeling and Flexible Docking: A Study of Musashi-1 Protein <{filename}/blog/2023-06-09-A-Structural-Refinement-Technique-for-Protein-RNA-Complexes-Using-Combination-of-AI-based-Modeling-and-Flexible-Docking-A-Study-of-Musashi-1-Protein.rst>`
  | Nitchakan Darai, Kowit Hengphasatporn, Peter Wolschann, :ul:`Michael T. Wolfinger`, Yasuteru Shigeta, Thanyada Rungrotmongkol, Ryuhei Harada
  | *B. Chem. Soc. Jpn.* 96(7):677–685 (2023) | :doi:`doi:10.1246/bcsj.20230092 <https://doi.org/10.1246/bcsj.20230092>` | :link-flat:`PDF <{static}/files/papers/Darai-2023.pdf>`
