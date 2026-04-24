Theoretical studies on RNA recognition by Musashi 1 RNA-binding protein
#######################################################################

:date: 2022-07-26
:modified: 2026-04-24
:tags: 3D; RNA-Protein interaction; AI
:category: publications
:slug: Theoretical-studies-on-RNA-recognition-by-Musashi1-RNA-binding-protein
:author: mtw
:summary: Molecular dynamics and binding-energy calculations are used here to compare how Musashi-1 recognizes different RNA motifs and to identify determinants of binding specificity.
:title: RNA recognition by Musashi-1
:description: Computational analysis of Musashi-1 RNA recognition using molecular dynamics simulations and binding-energy calculations.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

    .. figure:: {static}/files/papers/preview/Preview__Darai-2022.001small.webp
          :alt: Association complexes of Musashi-1 RBD1 and RBD2 with the canonical target RNA GUAGU 
          :figclass: m-figure m-flat



Musashi-1 (MSI1) is an RNA-binding protein involved in stem-cell maintenance, neural development, and post-transcriptional regulation. It also became particularly interesting in the context of Zika virus biology, because Musashi proteins were proposed to interact with viral RNAs in ways that could affect replication and neuropathology. That makes the underlying recognition problem more than a narrow structural question: understanding how Musashi binds RNA is relevant both for endogenous regulation and for virus-host interaction studies.

This paper focuses on that recognition step at the level of individual binding domains. MSI1 contains two RNA-binding domains, RBD1 and RBD2, both of which recognize short single-stranded RNA motifs centered on a UAG core. The main question is how specific that recognition really is. Sequence logos and motif descriptions are useful, but they do not explain why some candidate pentamers bind more strongly than others, or which contacts stabilize the preferred complexes.

The methodological approach is straightforward but well chosen for this kind of problem. The study starts from structural models for the Musashi RNA-binding domains and combines those with several candidate RNA pentamers. These protein-RNA complexes are then evaluated using atomistic molecular dynamics simulations in explicit solvent, followed by binding free-energy estimates using the solvated interaction energy framework. In practice, that means the paper does not rely on a single static docking pose. Instead, it asks whether the complexes remain stable over time and whether the interaction energies consistently favor some RNA motifs over others.

An additional point of interest is the use of AlphaFold2 to evaluate the protein side of the system. At the time, this was a useful check on whether predicted Musashi domain structures were close enough to experimentally determined conformations to support downstream simulation. The answer was essentially yes: the predicted structures aligned well with known domain architectures, which made it reasonable to use them as a basis for analyzing RNA recognition.

The main finding is that Musashi binding is selective even among short, closely related RNA pentamers. Out of the four tested motifs, two showed substantially stronger calculated binding to MSI1 RBD1 and RBD2 than the others. The simulations trace that difference back to a more favorable network of stacking, hydrogen-bonding, and electrostatic interactions around the central recognition motif. In other words, the work moves the discussion from “Musashi prefers UAG-containing RNAs” to a more specific structural claim about why some local sequence contexts are better accommodated than others.

That is what makes the paper useful. It does not claim to solve RNA-protein recognition in general, and it does not replace experiment. What it does provide is a mechanistic picture of how Musashi domains engage short RNA targets and how binding specificity can be compared systematically across candidate motifs. For systems where direct structural data are still incomplete, that kind of analysis is often the right intermediate step between motif discovery and functional testing.

This study also laid some groundwork for later Musashi modeling efforts. Once domain-level recognition preferences are characterized at this level, it becomes easier to ask larger questions about Musashi binding to structured cellular RNAs or to viral untranslated regions, and to develop more detailed protein-RNA complex refinement workflows. In that sense, this paper is best viewed as the starting point of a broader Musashi-RNA modeling program rather than a standalone binding-energy exercise.


.. frame:: Abstract

   The Musashi (MSI) family of RNA-binding proteins, comprising the two homologs Musashi-1 (MSI1) and Musashi-2 (MSI2), typically regulates translation and is involved in cell proliferation and tumorigenesis. MSI proteins contain two ribonucleoprotein-like RNA-binding domains, RBD1 and RBD2, that bind single-stranded RNA motifs with a central UAG trinucleotide with high affinity and specificity. The finding that MSI also promotes the replication of Zika virus, a neurotropic Flavivirus, has triggered further investigations of the biochemical principles behind MSI–RNA interactions. However, a detailed molecular understanding of the specificity of MSI RBD1/2 interaction with RNA is still missing. Here, we performed computational studies of MSI1–RNA association complexes, investigating different RNA pentamer motifs using molecular dynamics simulations with binding free energy calculations based on the solvated interaction energy method. Simulations with Alphafold2 suggest that predicted MSI protein structures are highly similar to experimentally determined structures. The binding free energies show that two out of four RNA pentamers exhibit a considerably higher binding affinity to MSI1 RBD1 and RBD2, respectively. The obtained structural information on MSI1 RBD1 and RBD2 will be useful for a detailed functional and mechanistic understanding of this type of RNA–protein interactions.

Figures and Data
================

.. image-grid::

  {static}/files/QuickSlide/QuickSlide__Darai-2022/QuickSlide__Darai-2022.001.png

  {static}/files/QuickSlide/QuickSlide__Darai-2022/QuickSlide__Darai-2022.002.png
  {static}/files/QuickSlide/QuickSlide__Darai-2022/QuickSlide__Darai-2022.003.png

  {static}/files/QuickSlide/QuickSlide__Darai-2022/QuickSlide__Darai-2022.004.png
  {static}/files/QuickSlide/QuickSlide__Darai-2022/QuickSlide__Darai-2022.005.png

  {static}/files/QuickSlide/QuickSlide__Darai-2022/QuickSlide__Darai-2022.006.png


Citation
========

  | :link-flat-strong:`Theoretical studies on RNA recognition by Musashi 1 RNA–binding protein <https://doi.org/10.1038/s41598-022-16252-w>`
  | Nitchakan Darai, Panupong Mahalapbutr, Peter Wolschann, Vannajan Sanghiran Lee, :ul:`Michael T. Wolﬁnger`, Thanyada Rungrotmongkol
  | *Sci. Rep.* 12:12137 (2022) | :doi:`doi:10.1038/s41598-022-16252-w <https://doi.org/10.1038/s41598-022-16252-w>` | :link-flat:`PDF <{static}/files/papers/Darai-2022.pdf>`

See Also
========

  | :link-flat-strong:`Musashi Binding Elements in Zika and Related Flavivirus 3’UTRs: A Comparative Study in Silico <{filename}/blog/2019-05-06-Musashi-Binding-Elements-in-Zika-and-Related-Flavivirus-3UTRs-A-Comparative-Study-in-Silico.rst>`
  | Adriano de Bernardi Schneider, :ul:`Michael T. Wolfinger`
  | *Sci. Rep.* 9(1):6911 (2019) | :doi:`doi:10.1038/s41598-019-43390-5 <https://doi.org/10.1038/s41598-019-43390-5>` | :link-flat:`PDF <{static}/files/papers/deBernardiSchneider-2019a.pdf>` | :link-flat:`Figures <{static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a.pdf>`

  | :link-flat-strong:`A Structural Refinement Technique for Protein-RNA Complexes Using a Combination of AI-based Modeling and Flexible Docking: A Study of Musashi-1 Protein <{filename}/blog/2023-06-09-A-Structural-Refinement-Technique-for-Protein-RNA-Complexes-Using-Combination-of-AI-based-Modeling-and-Flexible-Docking-A-Study-of-Musashi-1-Protein.rst>`
  | Nitchakan Darai, Kowit Hengphasatporn, Peter Wolschann, :ul:`Michael T. Wolfinger`, Yasuteru Shigeta, Thanyada Rungrotmongkol, Ryuhei Harada
  | *B. Chem. Soc. Jpn.* 96(7):677–685 (2023) | :doi:`doi:10.1246/bcsj.20230092 <https://doi.org/10.1246/bcsj.20230092>` | :link-flat:`PDF <{static}/files/papers/Darai-2023.pdf>`
