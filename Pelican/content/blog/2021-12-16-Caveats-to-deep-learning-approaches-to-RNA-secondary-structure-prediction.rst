Caveats to deep learning approaches to RNA secondary structure prediction
#########################################################################

:date: 2021-12-16
:modified: 2022-02-11
:tags: ViennaRNA
:category: publications
:slug: Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction
:author: mtw
:summary: How good are modern machine learning approaches in predicting the pairing potential of RNA (PREPRINT)

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. block-default:: Abstract

   Machine learning (ML) and in particular deep learning techniques have gained popularity for predicting structures from biopolymer sequences. An interesting case is the prediction of RNA secondary structures, where well established biophysics based methods exist. These methods even yield exact solutions under certain simplifying assumptions. Nevertheless, the accuracy of these classical methods is limited and has seen little improvement over the last decade. This makes it an attractive target for machine learning and consequently several deep learning models have been proposed in recent years. In this contribution we discuss limitations of current approaches, in particular due to biases in the training data. Furthermore, we propose to study capabilities and limitations of ML models by first applying them on synthetic data that can not only be generated in arbitrary amounts, but are also guaranteed to be free of biases. We apply this idea by testing several ML models of varying complexity. Finally, we show that the best models are capable of capturing many, but not all, properties of RNA secondary structures. Most severely, the number of predicted base pairs scales quadratically with sequence length, even though a secondary structure can only accommodate a linear number of pairs.

.. block-info:: Reference

  | :link-flat-strong:`Caveats to deep learning approaches to RNA secondary structure prediction <https://doi.org/10.1101/2021.12.14.472648>`
  |  Christoph Flamm, Julia Wielach, Michael T. Wolfinger, Stefan Badelt, Ivo L. Hofacker
  | *bioRxiv* 2021.12.14.472648 (2021) | :doi:`doi: 10.1101/2021.12.14.472648 <https://doi.org/10.1101/2021.12.14.472648>` | :link-flat:`Preprint PDF <{static}/files/papers/Flamm-2022__PREPRINT.pdf>`
