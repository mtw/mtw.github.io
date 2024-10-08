Barrier Trees of Degenerate Landscapes
######################################

:date: 2002-07-01
:modified: 2024-10-07
:tags: energy landscapes; new method; tools 
:category: publications
:slug: Barrier-Trees-of-Degenerate-Landscapes
:author: mtw
:summary: This method paper introduces the concept of barrier trees, a convenient approach to describe the landscape of an optimization function. Barrier trees represent the toplogical characteristics of an energy landscape, such as a unique partitioning into local minima as leaves of the tree and saddle points as internal nodes connecting different minima.
:description: 
:title: Barrier Trees of Degenerate Landscapes
:description: Introducing barrier trees: a method to visualize energy landscapes, highlighting local minima and saddle points, with the 'barriers' program for efficient computation.


.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

The decomposition of non-degenerate landscapes into basins surrounding local minima connected by saddle points is straightforward. This paper extends the concept to degenerate landscapes, where the situation is more complex. We present the program 'barriers' that efficiently computes barrier trees for degenerate landscapes. This approach involves discretizing the search space, and constructing the barrier tree from i) a a set of states, ii) a neighborhood relation between states, and iii) an energy of fitness function assigned to each state. The resulting topology is visualized as a tree, and made accessible for further processing.

.. raw:: html

  <object data="{static}/files/papers/Flamm-2002__PRPERINT.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Flamm-2002__PRPERINT.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

  The heights of energy barriers separating two (macro-)states are useful for estimating transition frequencies. In non-degenerate landscapes the decomposition of a landscape into basins surrounding local minima connected by saddle points is straightforward and yields a useful definition of macro-states. In this work we develop a rigorous concept of barrier trees for degenerate landscapes. We present a program that efficiently computes such barrier trees, and apply it to two well known examples of landscapes.
  

Citation
========

  | :link-flat-strong:`Barrier Trees of Degenerate Landscapes <https://doi.org/10.1524/zpch.2002.216.2.155>`
  | Christoph Flamm, Ivo L. Hofacker, Peter F. Stadler, :ul:`Michael T. Wolfinger`
  | *Z. Phys. Chem.* 216: 155–73 (2002) | :doi:`doi:10.1524/zpch.2002.216.2.155 <https://doi.org/10.1524/zpch.2002.216.2.155>` | :link-flat:`Preprint PDF <{static}/files/papers/Flamm-2002__PRPERINT.pdf>` 

See Also
========

  | :link-flat-strong:`Memory Efficient RNA Energy Landscape Exploration <{filename}/blog/2014-06-12-memory-efficient-RNA-energy-landscape-exploration.rst>`
  | Martin Mann, Marcel Kucharík, Christoph Flamm, :ul:`Michael T. Wolfinger`
  | *Bioinformatics* 30: 2584–91 (2014) | :doi:`doi:10.1093/bioinformatics/btu337 <https://doi.org/10.1093/bioinformatics/btu337>` | :link-flat:`PDF <{static}/files/papers/Mann-2014.pdf>` 

  | **BarMap: RNA Folding on Dynamic Energy Landscapes**
  | Ivo L. Hofacker, Christoph Flamm, Michael Heine, :ul:`Michael T. Wolfinger`, Gerik Scheuermann, Peter F. Stadler
  | *RNA* 16:1308–16 (2010) | :doi:`doi:10.1261/rna.2093310 <https://doi.org/10.1261/rna.2093310>` | :link-flat:`PDF <{static}/files/papers/Hofacker-2010.pdf>` 

  | **Exploring the Lower Part of Discrete Polymer Model Energy Landscapes**
  | :ul:`Michael T. Wolfinger`, Sebastian Will, Ivo L. Hofacker, Rolf Backofen, Peter F. Stadler
  | *Europhys. Lett.* 74(4): 726–32 (2006) | :doi:`doi:10.1209/epl/i2005-10577-0 <https://doi.org/10.1209/epl/i2005-10577-0>` | :link-flat:`Preprint PDF <{static}/files/papers/Wolfinger-2006__PREPRINT.pdf>` 

  | **Efficient Computation of RNA Folding Dynamics**
  | :ul:`Michael T. Wolfinger`, W. Andreas Svrcek-Seiler, Christoph Flamm, Ivo L. Hofacker, Peter F. Stadler
  | *J. Phys. A: Math. Gen.* 37(17): 4731–41 (2004) | :doi:`doi:10.1088/0305-4470/37/17/005 <https://doi.org/10.1088/0305-4470/37/17/005>` | :link-flat:`PDF <{static}/files/papers/Wolfinger-2004.pdf>`

