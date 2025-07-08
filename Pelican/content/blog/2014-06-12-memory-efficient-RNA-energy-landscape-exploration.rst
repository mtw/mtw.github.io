Memory-efficient-RNA-energy-landscape-exploration
#################################################

:date: 2014-06-12
:modified: 2022-10-14
:tags: energy landscapes; new method; tools
:category: publications
:slug: Memory-efficient-RNA-energy-landscape-exploration
:author: mtw
:summary: Discrete energy landscapes provide a valuable means for analyzing non-equilibrium properties of biopolymers. In this study we propose a memory-efficient approach for local flooding of the lower portion of an RNA folding landscape
:description: A memory efficient approach for exploring the low-energy portion of RNA energy landscapes at the level of secondary structures
:title: How to efficiently explore the lower portion of RNA energy landscapes

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

The dynamic process of RNA folding can be modeled as a continuous-time Markov process, focusing on local minima, their associated basins of attraction, and the saddle points that connect them.

To construct an energy landscape, a connected set of RNA structures, commonly referred to as the state space, is required, along with a neighborhood relation between these states and an assigned energy or fitness value. Although obtaining the complete suboptimal folding for RNA sequences longer than 100 nucleotides is computationally impractical, various strategies have been developed to explore the lower-energy portion of the landscape.

In this work, we introduce a local variant of our previous global flooding approach to energy landscapes. This localized flooding technique significantly reduces memory usage, allowing for the analysis of energy landscapes for longer RNA sequences.

.. raw:: html

  <object data="{static}/files/papers/Mann-2014.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs.
     <a href="{static}/files/papers/Mann-2014.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

    **Motivation:** Energy landscapes provide a valuable means for studying the
    folding dynamics of short RNA molecules in detail by modeling all
    possible structures and their transitions. Higher abstraction levels
    based on a macro-state decomposition of the landscape enable the study of
    larger systems; however, they are still restricted by huge memory
    requirements of exact approaches.

    **Results:** We present a highly parallelizable local enumeration scheme that
    enables the computation of exact macro-state transition models with
    highly reduced memory requirements. The approach is evaluated on RNA
    secondary structure landscapes using a gradient basin definition for
    macro-states. Furthermore, we demonstrate the need for exact transition
    models by comparing two barrier-based approaches, and perform a detailed
    investigation of gradient basins in RNA energy landscapes.

    **Availability and implementation:** Source code is part of the :link:`C++ Energy Landscape Library <https://www.bioinf.uni-freiburg.de/subpage/software/libraries.html#lib_ell>`.

Citation
========

  | :link-flat-strong:`Memory-efficient RNA energy landscape exploration <http://bioinformatics.oxfordjournals.org/content/30/18/2584>`
  | Martin Mann, Marcel Kucharík, Christoph Flamm, Michael T. Wolfinger
  | *Bioinformatics* 30(18):2584-2591 (2014) | :doi:`doi: 10.1093/bioinformatics/btu337 <https://doi.org/10.1093/bioinformatics/btu337>` | :link-flat:`PDF <{static}/files/papers/Mann-2014.pdf>`

See Also
========

  | :link-flat-strong:`Exploring the Lower Part of Discrete Polymer Model Energy Landscapes <{filename}/blog/2006-04-14-Exploring-the-Lower-Part-of-Discrete-Polymer-Model-Energy-Landscapes.rst>``
  | :ul:`Michael T. Wolfinger`, Sebastian Will, Ivo L. Hofacker, Rolf Backofen, Peter F. Stadler
  | *Europhys. Lett.* 74(4): 726–32 (2006) | :doi:`doi:10.1209/epl/i2005-10577-0 <https://doi.org/10.1209/epl/i2005-10577-0>` | :link-flat:`Preprint PDF <{static}/files/papers/Wolfinger-2006__PREPRINT.pdf>`

  | :link-flat-strong:`Barrier Trees of Degenerate Landscapes <{filename}/blog/2002-07-01-Barrier_Trees_of_Degenerate_Landscapes.rst>`
  | Christoph Flamm, Ivo L. Hofacker, Peter F. Stadler, :ul:`Michael T. Wolfinger`
  | *Z. Phys. Chem.* 216: 155–73 (2002) | :doi:`doi:10.1524/zpch.2002.216.2.155 <https://doi.org/10.1524/zpch.2002.216.2.155>` | :link-flat:`Preprint PDF <{static}/files/papers/Flamm-2002__PRPERINT.pdf>`
