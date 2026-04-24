Efficient Computation of Cotranscriptional RNA-Ligand Interaction Dynamics
##########################################################################

:date: 2018-07-01
:modified: 2022-10-14
:tags: energy landscapes; new method; RNA folding kinetics; ViennaRNA; synthetic biology; co-transcriptional RNA folding
:category: publications
:slug: Efficient-Computation-of-Cotranscriptional-RNA-Ligand-Interaction-Dynamics
:author: mtw
:summary: A ViennaRNA-based approach for modeling cotranscriptional RNA-ligand interaction dynamics in kinetically controlled riboswitches.
:title: Co-transcriptional riboswitch modeling with ViennaRNA
:description: Co-transcriptional RNA folding under kinetic control can be efficiently modeled with computational approaches for the 2'dG riboswitch.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi


At the heart of the methodology lies an extension of the BARRIERS approach, partitioning the folding landscape into distinct classes of structures based on the presence or absence of ligands. By adopting an all-or-none scenario for ligand binding, we efficiently model concentration-dependent binding and unbinding events, offering a glimpse into the dynamic behavior of riboswitches under kinetic control. Through a modified version of the BARMAP pipeline, co-transcriptional folding dynamics are meticulously computed.

Using the I-A 2’-deoxyguanosine (2’dG)-sensing riboswitch from Mesoplasma florum, which has recently been studied by NMR spectroscopy, as an example we show that our results are in good agreement with experimental data. Computational predictions yield substantial mechanistic insight, allowing us not only to understand natural riboswitches on a mechanistic level but also to perform systematic in silico screening and analysis of novel designs before expensive experimental validation.

This technical study advances our understanding of riboswitch folding dynamics and offers a computational tool for engineering riboswitch-based gene regulation in synthetic biology applications.

.. frame:: Abstract

  Riboswitches form an abundant class of cis-regulatory RNA elements that mediate gene expression by binding a small metabolite. For synthetic biology applications, they are becoming cheap and accessible systems for selectively triggering transcription or translation of downstream genes. Many riboswitches are kinetically controlled, hence knowledge of their co-transcriptional mechanisms is essential. We present here an efficient implementation for analyzing co-transcriptional RNA-ligand interaction dynamics. This approach allows for the first time to model concentration-dependent metabolite binding/unbinding kinetics. We exemplify this novel approach by means of the recently studied I-A 2′-deoxyguanosine (2′dG)-sensing riboswitch from Mesoplasma florum.

Citation
========

  | :link-flat-strong:`Efficient Computation of Cotranscriptional RNA-Ligand Interaction Dynamics <https://doi.org/10.1016/j.ymeth.2018.04.036>`
  | :ul:`Michael T. Wolfinger`, Christoph Flamm, Ivo L. Hofacker
  | *Methods* 143:70–76 (2018) | :doi:`doi: 10.1016/j.ymeth.2018.04.036 <https://doi.org/10.1016/j.ymeth.2018.04.036>` | :link-flat:`PDF <{static}/files/papers/Wolfinger-2018__PREPRINT.pdf>`

See Also
========

  | :link-flat-strong:`NMR Structural Profiling of Transcriptional Intermediates Reveals Riboswitch Regulation by Metastable RNA Conformations <{filename}/blog/2017-01-31-NMR-Structural-Profiling-of-Transcriptional-Intermediates-Reveals-Riboswitch-Regulation-by-Metastable-RNA-Conformations.rst>`
  | Christina Helmling, Anna Wacker, :ul:`Michael T. Wolfinger`, Ivo L. Hofacker, Martin Hengsbach, Boris Fürtig, Harald Schwalbe
  | *J. Am. Chem. Soc.* 139 (7):2647–56 (2017) | :doi:`doi:10.1021/jacs.6b10429 <https://doi.org/10.1021/jacs.6b10429>`
