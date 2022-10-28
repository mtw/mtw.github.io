Caveats to deep learning approaches to RNA secondary structure prediction
#########################################################################

:date: 2021-12-16
:modified: 2022-10-29
:tags: ViennaRNA
:category: publications
:slug: Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction
:author: mtw
:title: Current deep learning methods unable to predict RNA secondary structures
:description: Published AI approaches for RNA structure prediction suffer from massively biased training sets, resulting in severely degraded prediction quality on arbitrary RNAs
:summary: Machine learning of RNA structure is more challenging than you might think. Using synthetic data from ViennaRNA's RNAfold to study the capabilities and shortcomings of neural networks for RNA secondary structure prediction in a controlled setting, we argue that shortcomings in the artificial setting will translate to real data

Published AI approaches for RNA structure prediction suffer from massively biased training sets, resulting in severely degraded prediction quality on arbitrary RNAs. Using inverse RNA folding, i.e. generating sequences that are compatible with a given structure, we generate synthetic data with the same bias as published deep learning approaches. A network trained on this set performs well on sequences that have no sequence similarity but fold into structures contained in the training set. On sequences with unrelated structures performance falls drastically. Thus, the network generalizes well to new sequences, but not to new structures.

Intriguingly, published deep learning methods on unbiased sets are not even capable of predicting correct RNA base pairing, a problem that is much simpler than the RNA folding problem. On top of that, BLSTMs predict pseudoknots and base triplets, although they do not occur in the ViennaRNA RNAfold ground truth.

Read the full story in our article 'Caveats to Deep Learning Approaches to RNA Secondary Structure Prediction', published in 'Frontiers in Bioinformatics'.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. button-primary:: {static}/files/papers/Flamm-2022.pdf

    Download PDF

.. frame:: Abstract


   Machine learning (ML) and in particular deep learning techniques have gained popularity for predicting structures from biopolymer sequences. An interesting case is the prediction of RNA secondary structures, where well established biophysics based methods exist. These methods even yield exact solutions under certain simplifying assumptions. Nevertheless, the accuracy of these classical methods is limited and has seen little improvement over the last decade. This makes it an attractive target for machine learning and consequently several deep learning models have been proposed in recent years. In this contribution we discuss limitations of current approaches, in particular due to biases in the training data. Furthermore, we propose to study capabilities and limitations of ML models by first applying them on synthetic data that can not only be generated in arbitrary amounts, but are also guaranteed to be free of biases. We apply this idea by testing several ML models of varying complexity. Finally, we show that the best models are capable of capturing many, but not all, properties of RNA secondary structures. Most severely, the number of predicted base pairs scales quadratically with sequence length, even though a secondary structure can only accommodate a linear number of pairs.

Figures and Data
================

.. image-grid::

  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.001.png

  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.002.png
  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.003.png

  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.004.png
  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.005.png

  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.006.png
  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.007.png

  {static}/files/QuickSlide/QuickSlide__Flamm-2022/QuickSlide__Flamm-2022.008.png

Citation
========

  | :link-flat-strong:`Caveats to deep learning approaches to RNA secondary structure prediction <https://doi.org/10.3389/fbinf.2022.835422>`
  | Christoph Flamm, Julia Wielach, :ul:`Michael T. Wolfinger`, Stefan Badelt, Ronny Lorenz, Ivo L. Hofacker
  | *Front. Bioinform.* 2:835422 (2022) | :doi:`doi:10.3389/fbinf.2022.835422 <https://doi.org/10.3389/fbinf.2022.835422>` | :link-flat:`PDF <{static}/files/papers/Flamm-2022.pdf>`

..
  .. block-info:: Citations

      .. container:: m-label

          .. raw:: html

            <span class="__dimensions_badge_embed__" data-doi="10.3389/fbinf.2022.835422" data-style="small_rectangle"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>

      .. container:: m-label

          .. raw:: html

            <script type="text/javascript" src="https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"></script><div class="altmetric-embed" data-badge-type="2" data-badge-popover="bottom" data-doi="10.3389/fbinf.2022.835422"></div>
