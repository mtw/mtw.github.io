Efficient Computation of RNA Folding Dynamics
#############################################

:date: 2004-04-14
:modified: 2026-04-24
:tags: RNA folding kinetics; energy landscapes
:category: publications
:slug: efficient-computation-rna-folding-dynamics
:author: mtw
:summary: This paper shows how barrier trees and numerical integration can approximate RNA folding dynamics efficiently enough to analyze bistable molecules and RNA switches on biologically relevant timescales.
:title: Efficient computation of RNA folding dynamics
:description: A barrier-tree based approach for efficient approximation of RNA folding dynamics within the secondary-structure energy landscape.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/shot__Wolfinger-2004.png
          :alt: RNA folding dynamics on a coarse-grained energy landscape
          :figclass: m-figure m-flat

This paper addresses a classical problem in RNA folding kinetics: exact or near-exact stochastic simulation quickly becomes expensive, but many biologically interesting questions depend on the dynamic behavior of secondary-structure landscapes rather than on a single minimum-energy fold. The solution proposed here is to coarse-grain the secondary-structure landscape using barrier trees built from local minima and their connecting saddle points.

Within that framework, RNA folding dynamics can be approximated by a master-equation approach on macrostates rather than on the full structure space. Instead of simulating huge numbers of trajectories, one numerically integrates the population flow between barrier-separated basins of attraction. This makes it possible to recover the folding behavior of bistable RNAs and metastable switches with much higher computational efficiency than direct trajectory-based simulations.

The important point is not just speed. Barrier trees provide a natural way to connect energy landscapes with kinetics, because they preserve the local minima, the barriers between them, and therefore the transitions most relevant for folding pathways. In the paper, the resulting dynamics agree reasonably well with stochastic folding simulations while extending the accessible timescales and molecule sizes. At the time, this was a significant step toward making RNA folding kinetics computationally tractable beyond toy examples.

This work is also foundational for later developments in RNA energy-landscape analysis. Many subsequent approaches to metastability, coarse-grained kinetics, and dynamic landscape mapping build on the same idea that one can separate the enormous RNA structure space into kinetically meaningful basins and work at that level instead of trying to resolve every elementary step directly.

For today’s readers, the paper remains relevant because it frames `RNA folding kinetics` as an energy-landscape problem rather than just a simulation problem. That perspective is still central when thinking about RNA switches, delayed folding, metastable intermediates, and the design of molecules whose function depends on how they move through structure space rather than only on where they end up.

.. raw:: html

  <object data="{static}/files/papers/Wolfinger-2004.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs.
     <a href="{static}/files/papers/Wolfinger-2004.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

   Barrier trees consisting of local minima and their connecting saddle points imply a natural coarse-graining for the description of the energy landscape of RNA secondary structures. Here we show that, based on this approach, it is possible to predict the folding behaviour of RNA molecules by numerical integration. Comparison with stochastic folding simulations shows reasonable agreement of the resulting folding dynamics and a drastic increase in computational efficiency that makes it possible to investigate the folding dynamics of RNA of at least tRNA size. Our approach is readily applicable to bistable RNA molecules and promises to facilitate studies on the dynamic behaviour of RNA switches.

Citation
========

  | :link-flat-strong:`Efficient Computation of RNA Folding Dynamics <{filename}/blog/2004-04-14-Efficient-Computation-of-RNA-Folding-Dynamics.rst>`
  | :ul:`Michael T. Wolfinger`, W. Andreas Svrcek-Seiler, Christoph Flamm, Ivo L. Hofacker, Peter F. Stadler
  | *J. Phys. A: Math. Gen.* 37(17):4731–4741 (2004) | :doi:`doi:10.1088/0305-4470/37/17/005 <https://doi.org/10.1088/0305-4470/37/17/005>` | :link-flat:`PDF <{static}/files/papers/Wolfinger-2004.pdf>`

