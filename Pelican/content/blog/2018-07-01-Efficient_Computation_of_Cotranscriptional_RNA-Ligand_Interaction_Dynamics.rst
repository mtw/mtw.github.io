Efficient Computation of Cotranscriptional RNA-Ligand Interaction Dynamics
##########################################################################

:date: 2018-07-01
:modified: 2022-10-14
:tags: energy landscapes; RNA kinetics; bacteria; ViennaRNA; synthetic biology
:category: publications
:slug: Efficient-Computation-of-Cotranscriptional-RNA-Ligand-Interaction-Dynamics
:author: mtw
:summary: Riboswitches are RNA molecules that regulate gene expression by sensing metabolites, presenting an interesting target for synthetic biology applications. We present a computational approach based on ViennaRNA tools to dissect and model RNA-ligand interaction dynamics under kinetic control, enabling simulation of riboswitch folding
:description: Co-transcriptional RNAfolding under kinetic control can be efficiently modeled with computational biology approaches for the 2'dG riboswitch
:title: Co-transcriptional riboswitch modleing with ViennaRNA
:description: Explore riboswitch potential with ViennaRNA tools for precise RNA-ligand interaction predictions and folding simulations in synthetic biology.

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

.. button-primary:: {static}/files/papers/Wolfinger-2018__PREPRINT.pdf

    Download PDF

.. frame:: Abstract

  Riboswitches form an abundant class of cis-regulatory RNA elements that mediate gene expression by binding a small metabolite. For synthetic biology applications, they are becoming cheap and accessible systems for selectively triggering transcription or translation of downstream genes. Many riboswitches are kinetically controlled, hence knowledge of their co-transcriptional mechanisms is essential. We present here an efficient implementation for analyzing co-transcriptional RNA-ligand interaction dynamics. This approach allows for the first time to model concentration-dependent metabolite binding/unbinding kinetics. We exemplify this novel approach by means of the recently studied I-A 2′-deoxyguanosine (2′dG)-sensing riboswitch from Mesoplasma florum.

Citation
========

  | :link-flat-strong:`Efficient Computation of Cotranscriptional RNA-Ligand Interaction Dynamics <https://doi.org/10.1016/j.ymeth.2018.04.036>`
  | Michael T. Wolfinger, Christoph Flamm, Ivo L. Hofacker
  | *Methods* 143:70–76 (2018) | :doi:`doi: 10.1016/j.ymeth.2018.04.036 <https://doi.org/10.1016/j.ymeth.2018.04.036>` | :link-flat:`PDF <{static}/files/papers/Wolfinger-2018__PREPRINT.pdf>`

See Also
========

  | :link-flat-strong:`NMR Structural Profiling of Transcriptional Intermediates Reveals Riboswitch Regulation by Metastable RNA Conformations <{filename}/blog/2017-01-31-NMR-Structural-Profiling-of-Transcriptional-Intermediates-Reveals-Riboswitch-Regulation-by-Metastable-RNA-Conformations.rst>`
  | Christina Helmling, Anna Wacker, :ul:`Michael T. Wolfinger`, Ivo L. Hofacker, Martin Hengsbach, Boris Fürtig, Harald Schwalbe
  | *J. Am. Chem. Soc.* 139 (7):2647–56 (2017) | :doi:`doi:10.1021/jacs.6b10429 <https://doi.org/10.1021/jacs.6b10429>`


..
  .. block-info:: Citations

    .. container:: m-label

        .. raw:: html

          <span class="__dimensions_badge_embed__" data-doi="10.1016/j.ymeth.2018.04.036" data-style="small_rectangle"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>

    .. container:: m-label

        .. raw:: html

          <script type="text/javascript" src="https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"></script><div class="altmetric-embed" data-badge-type="2" data-badge-popover="bottom" data-doi="10.1016/j.ymeth.2018.04.036"></div>
