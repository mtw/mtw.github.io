KinPFN: Bayesian Approximation of RNA Folding Kinetics
######################################################

:date: 2025-01-01
:modified: 2026-04-24
:tags: RNA folding kinetics; AI
:category: publications
:slug: kinpfn-rna-folding-kinetics
:author: mtw
:summary: KinPFN uses prior-data fitted networks to approximate first-passage-time distributions for RNA folding kinetics orders of magnitude faster than direct simulation.
:title: KinPFN for RNA folding kinetics
:description: A deep-learning approach to approximate RNA folding-time distributions from a few simulated examples.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Scheuer-2025.001small.webp
          :alt: KinPFN training on a synthetic prior of RNA folding time distributions
          :figclass: m-figure m-flat

RNA folding kinetics is often summarized in terms of first passage times: how long it takes a molecule to reach a target structure for the first time. Those distributions are informative because they capture more than a single mean folding time, but obtaining them requires many stochastic simulations and quickly becomes expensive. This paper asks whether the entire folding-time distribution can be approximated directly from a small number of example simulations.

The proposed answer is KinPFN, a prior-data fitted network trained on synthetic multi-modal distributions that mimic the shape of RNA first-passage-time distributions. Instead of learning from large collections of labeled RNA molecules, the model is trained to do approximate Bayesian inference on generic folding-time distributions. At application time, it receives only a few observed folding times as context and predicts the full cumulative distribution function in a single forward pass.

That framing is important. The method is not replacing physical simulators with a black box trained on a fixed benchmark set. It is designed as a fast probabilistic approximation layer that can sit on top of existing kinetics tools such as Kinfold and return a useful estimate of the folding-time distribution long before exhaustive simulation would finish. In practice, the paper reports speed-ups of at least 95% while preserving the overall shape of the distribution sufficiently well for downstream analysis.

The real value of the approach is that it makes distribution-level reasoning about folding kinetics much more accessible. Instead of reducing kinetics to a single summary statistic, one can compare broad versus narrow first-passage distributions, detect inefficient folding processes, and screen many more candidates than direct simulation alone would allow. The paper illustrates this in analyses of eukaryotic RNAs and folding-efficiency case studies, where the quality of the approximation is already good enough to be practically informative.

For RNA folding kinetics this is a useful conceptual shift. It shows that machine learning can accelerate kinetic analysis without having to learn RNA folding from scratch. By focusing on posterior approximation rather than direct structure prediction, KinPFN becomes a practical tool for kinetic RNA design workflows, where many candidate sequences need to be compared quickly but full simulation remains computationally restrictive.

.. raw:: html

  <object data="{static}/files/papers/Scheuer-2025.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs.
     <a href="{static}/files/papers/Scheuer-2025.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

   RNA is a dynamic biomolecule crucial for cellular regulation, with its function largely determined by its folding into complex structures, while misfolding can lead to multifaceted biological sequelae. During the folding process, RNA traverses through a series of intermediate structural states, with each transition occurring at variable rates that collectively influence the time required to reach the functional form. Understanding these folding kinetics is vital for predicting RNA behavior and optimizing applications in synthetic biology and drug discovery. While in silico kinetic RNA folding simulators are often computationally intensive and time-consuming, accurate approximations of the folding times can already be very informative to assess the efficiency of the folding process. In this work, we present KinPFN, a novel approach that leverages prior-data fitted networks to directly model the posterior predictive distribution of RNA folding times. By training on synthetic data representing arbitrary prior folding times, KinPFN efficiently approximates the cumulative distribution function of RNA folding times in a single forward pass, given only a few initial folding time examples. Our method offers a modular extension to existing RNA kinetics algorithms, promising significant computational speed-ups orders of magnitude faster, while achieving comparable results.

Citation
========

  | :link-flat-strong:`KinPFN: Bayesian Approximation of RNA Folding Kinetics using Prior-Data Fitted Networks <{filename}/blog/2025-01-01-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst>`
  | Dominik Scheuer, Frederic Runge, Jörg K.H. Franke, :ul:`Michael T. Wolfinger`, Christoph Flamm, Frank Hutter
  | *The Thirteenth International Conference on Learning Representations (ICLR'25)* (2025) | :doi:`doi:10.5281/zenodo.15233965 <https://doi.org/10.5281/zenodo.15233965>` | :link-flat:`PDF <{static}/files/papers/Scheuer-2025.pdf>`

