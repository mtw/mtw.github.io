Barrier Trees of Degenerate Landscapes
######################################

:date: 2002-07-01
:modified: 2026-04-24
:tags: energy landscapes; new method; tools 
:category: publications
:slug: Barrier-Trees-of-Degenerate-Landscapes
:author: mtw
:summary: This paper develops the barrier-tree formalism for degenerate landscapes and helped establish a general language for analyzing basins, saddle points, and transition barriers in complex discrete systems.
:title: Barrier Trees of Degenerate Landscapes
:description: A foundational paper on barrier trees for degenerate landscapes and on the barriers software for coarse-grained energy-landscape analysis.


.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

This is one of the earliest papers in the landscape-analysis thread that later became central to my work on RNA folding kinetics. It is also one of the most mathematical. But the reason it became widely cited is actually quite practical: it gave people a compact and rigorous way to describe the large-scale topology of complex discrete landscapes.

The core problem is easy to state. If a system has many local minima, one needs some way to summarize which minima belong to which basins, where the relevant saddle points lie, and how difficult it is to move from one basin to another. In non-degenerate landscapes, that decomposition is conceptually straightforward. In degenerate landscapes, however, many states can share the same energy, and the clean separation into minima, saddles, and basins becomes much less obvious. That is exactly the setting this paper addresses.

The contribution of the paper is to extend the concept of a barrier tree to such degenerate cases and to implement that formalism in the `barriers` program. The input is deliberately general: one needs only a finite set of states, a neighborhood relation, and an energy or fitness value assigned to each state. From that information, the method constructs a tree in which leaves correspond to minima or minimal basins and internal nodes represent the saddle-like connections that merge them at increasing energy thresholds.

Why is that useful? Because the tree compresses a huge and otherwise unmanageable state space into something interpretable. Instead of staring at an enormous graph of configurations, one obtains a hierarchical representation of the landscape: which minima are close, which barriers are high, and which large-scale basins dominate the topology. That immediately makes the landscape more accessible for kinetics, visualization, and coarse graining.

This is also the point where the paper moves beyond pure mathematical formalism. Once barriers are represented explicitly, they can be used to estimate transition frequencies and to define macrostates for dynamical models. That connection turned out to be extremely important. Much of the later work on RNA energy landscapes, metastability, folding kinetics, and dynamic landscape mapping depends on exactly this move from raw microstates to a barrier-structured macrostate view.

Another reason the paper has aged well is that it is not specific to RNA. The formalism is deliberately problem-independent and applies to discrete landscapes more broadly, including spin systems, lattice models, and other optimization settings. That generality made barrier trees useful outside their original context and helped establish them as a standard conceptual tool in landscape analysis.

For readers coming from RNA biology, the significance of this paper is easiest to appreciate in hindsight. Many later methods in this blog, including coarse-grained RNA folding kinetics and the exploration of dynamic landscapes, rely on the assumption that one can meaningfully partition structure space into basins connected by barriers. This 2002 paper is one of the places where that assumption was made rigorous for degenerate discrete systems.

So while the article is mathematically inclined, the underlying message is simple and still relevant: if you want to understand a complex landscape, you need more than a list of low-energy states. You need a representation of how those states are connected. Barrier trees provided exactly that representation, and the `barriers` tool made it computationally usable.

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

  | :link-flat-strong:`BarMap: RNA Folding on Dynamic Energy Landscapes <{filename}/blog/2010-07-01-BarMap-RNA-Folding-on-Dynamic-Energy-Landscapes.rst>`
  | Ivo L. Hofacker, Christoph Flamm, Michael Heine, :ul:`Michael T. Wolfinger`, Gerik Scheuermann, Peter F. Stadler
  | *RNA* 16:1308–16 (2010) | :doi:`doi:10.1261/rna.2093310 <https://doi.org/10.1261/rna.2093310>` | :link-flat:`PDF <{static}/files/papers/Hofacker-2010.pdf>` 

  | :link-flat-strong:`Exploring the Lower Part of Discrete Polymer Model Energy Landscapes <{filename}/blog/2006-04-14-Exploring-the-Lower-Part-of-Discrete-Polymer-Model-Energy-Landscapes.rst>`
  | :ul:`Michael T. Wolfinger`, Sebastian Will, Ivo L. Hofacker, Rolf Backofen, Peter F. Stadler
  | *Europhys. Lett.* 74(4): 726–32 (2006) | :doi:`doi:10.1209/epl/i2005-10577-0 <https://doi.org/10.1209/epl/i2005-10577-0>` | :link-flat:`Preprint PDF <{static}/files/papers/Wolfinger-2006__PREPRINT.pdf>` 

  | :link-flat-strong:`Efficient Computation of RNA Folding Dynamics <{filename}/blog/2004-04-14-Efficient-Computation-of-RNA-Folding-Dynamics.rst>`
  | :ul:`Michael T. Wolfinger`, W. Andreas Svrcek-Seiler, Christoph Flamm, Ivo L. Hofacker, Peter F. Stadler
  | *J. Phys. A: Math. Gen.* 37(17): 4731–41 (2004) | :doi:`doi:10.1088/0305-4470/37/17/005 <https://doi.org/10.1088/0305-4470/37/17/005>` | :link-flat:`PDF <{static}/files/papers/Wolfinger-2004.pdf>`
