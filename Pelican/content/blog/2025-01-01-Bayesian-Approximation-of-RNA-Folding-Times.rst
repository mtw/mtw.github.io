Bayesian Approximation of RNA Folding Times
###########################################

:date: 2025-01-01
:modified: 2026-04-24
:tags: RNA folding kinetics; AI
:category: publications
:slug: bayesian-approximation-rna-folding-times
:author: mtw
:summary: This workshop paper introduces the core KinPFN idea: approximating RNA first-passage-time distributions with a prior-data fitted network trained on synthetic folding-time priors.
:title: Bayesian approximation of RNA folding times
:description: A workshop paper on using prior-data fitted networks to approximate RNA folding-time distributions from a few context examples.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Scheuer-2025__AI4NA.001small.webp
          :alt: Bayesian approximation of RNA folding times with KinPFN
          :figclass: m-figure m-flat

This workshop paper presents the core idea behind KinPFN in a compact form: model RNA folding-time distributions directly, instead of recomputing them through thousands of simulator runs for every new case. The target quantity is the cumulative distribution of first passage times, a useful kinetic summary because it reflects how quickly different fractions of molecules reach a structure of interest.

The proposed solution uses prior-data fitted networks, trained not on a large corpus of experimentally measured RNAs, but on synthetic multi-modal distributions chosen to resemble the behavior of real folding-time data. Given just a few example folding times from a kinetics simulator, the model predicts the posterior distribution of folding times and from that the full cumulative distribution function. That makes the method especially attractive where only a small kinetic sample is available but a full distribution estimate would be useful.

What makes this interesting for RNA folding kinetics is the combination of speed and modularity. The method does not require rewriting the underlying simulator or abandoning physically motivated kinetic models. Instead, it acts as an approximation layer that reduces the number of expensive simulations needed for downstream interpretation. The workshop paper therefore functions as a proof of principle for integrating modern probabilistic machine learning into RNA kinetics workflows.

Relative to the full conference paper, this version is shorter and more focused on the central idea, but it already makes the key argument clearly: approximating folding-time distributions can be enough for many practical tasks, and those approximations can be learned efficiently from a synthetic prior. For anyone interested in the intersection of RNA folding kinetics and AI, this paper is a useful entry point into the broader KinPFN project.

.. raw:: html

  <object data="{static}/files/papers/Scheuer-2025__AI4NA.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs.
     <a href="{static}/files/papers/Scheuer-2025__AI4NA.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

   RNA is a dynamic biomolecule with its function largely determined by its folding into complex structures. During the folding process, an RNA traverses through a series of intermediate structural states, with each transition occurring at variable rates that collectively influence the time required to reach the functional form. Understanding these folding kinetics is vital for predicting RNA behavior and optimizing applications in synthetic biology and drug discovery. While in silico kinetic RNA folding simulators are often computationally intensive and time-consuming, accurate approximations of the folding times can already be very informative to assess the efficiency of the folding process. Here, we present KinPFN, a novel approach that leverages prior-data fitted networks to directly model the posterior predictive distribution of RNA folding times. Trained on synthetic data representing arbitrary prior folding times, KinPFN efficiently approximates the cumulative distribution function of RNA folding times in a single forward pass, given only a few initial folding time examples. Our method offers a modular extension to RNA kinetics algorithms, promising significant computational speed-ups orders of magnitude faster, while achieving comparable results.

Citation
========

  | :link-flat-strong:`Bayesian Approximation of RNA Folding Times <{filename}/blog/2025-01-01-Bayesian-Approximation-of-RNA-Folding-Times.rst>`
  | Dominik Scheuer, Frederic Runge, Jörg K.H. Franke, :ul:`Michael T. Wolfinger`, Christoph Flamm, Frank Hutter
  | *ICLR 2025 Workshop on AI for Nucleic Acids* (2025) | :doi:`doi:10.5281/zenodo.15228717 <https://doi.org/10.5281/zenodo.15228717>` | :link-flat:`PDF <{static}/files/papers/Scheuer-2025__AI4NA.pdf>`

