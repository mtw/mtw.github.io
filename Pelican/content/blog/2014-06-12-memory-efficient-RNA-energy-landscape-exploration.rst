Memory-efficient-RNA-energy-landscape-exploration
#################################################

:date: 2014-06-12
:modified: 2022-02-09
:tags: RNA
:category: publications
:slug: Memory-efficient-RNA-energy-landscape-exploration.
:authors: mtw
:summary: A efficient approach for local flooding of the lower portion of an RNA energy landscape

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Discrete energy landscapes provide a valuable means for analyzing
non-equilibrium properties of biopolymers. RNA folding dynamics, for
example, can be described by a continuous-time Markov process at the level
of local minima, their corresponding basins of attraction and saddle points
connecting them.

A connected set of structures, often denoted *state space* is required for
energy landscape construction. While complete suboptimal folding of RNA is
practically impossible for chain lengths above 100nt, alternative
strategies to enumerate the lower part of the energy landscape emerged over
the last years.

We have recently extended previous work on global flooding by a local
flooding approach that minimizes memory consumption and published the
method in *Bioinformatics*.

.. block-default:: Abstract

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

    **Availability and implementation:** Source code is part of the C++ Energy
    Landscape Library available at http://www.bioinf.uni-freiburg.de/Software/.


.. block-info:: Reference

  | :link-flat-strong:`Memory-efficient RNA energy landscape exploration <http://bioinformatics.oxfordjournals.org/content/30/18/2584>`
  | Martin Mann, Marcel Kucharík, Christoph Flamm, Michael T. Wolfinger
  | *Bioinformatics* 30(18):2584-2591 (2014) | :doi:`doi:10.1093/bioinformatics/btu337 <https://doi.org/10.1093/bioinformatics/btu337>` | :link-flat:`PDF <{static}/files/papers/Mann-2014.pdf>`
