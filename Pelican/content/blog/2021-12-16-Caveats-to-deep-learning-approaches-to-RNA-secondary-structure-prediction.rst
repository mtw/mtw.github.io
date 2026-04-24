Caveats to deep learning approaches to RNA secondary structure prediction
#########################################################################

:date: 2021-12-16
:modified: 2026-04-24
:tags: ViennaRNA; AI
:category: publications
:slug: Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction
:author: mtw
:title: Caveats in deep learning for RNA secondary structure prediction
:description: A closer look at why many deep learning models for RNA secondary structure prediction appear to work well, yet often fail to generalize beyond biased benchmark datasets.
:summary: This paper shows that many deep learning models for RNA secondary structure prediction learn dataset bias more readily than RNA folding rules, and explains why that matters for the future of AI in RNA biology.

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Flamm-2022.001small.webp
          :alt: Input/output encoding for predicting RNA paired/unpaired status using a BLSTM
          :figclass: m-figure m-flat

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Deep learning for RNA secondary structure prediction has an obvious appeal: if neural networks can infer structure directly from sequence, perhaps they can leap past the limitations of classical thermodynamic folding. That promise has made the area popular, but it also created a familiar problem from other corners of machine learning: impressive benchmark numbers can hide the fact that a model has learned properties of the dataset rather than properties of the underlying biology.

That is the central concern of this paper. Instead of asking only whether a model performs well on a standard test split, we ask what exactly it has learned. Has it captured transferable principles of RNA folding, or has it mostly memorized the structural biases of the RNAs it was shown during training? For RNA structure prediction, that distinction matters a great deal, because the real task is not to recognize another tRNA-like example from a familiar family. It is to say something useful about RNAs with new sequence-structure relationships.

The methodological approach is deliberately controlled. We use inverse RNA folding to generate synthetic datasets with known structural properties, which lets us vary the amount of bias in the training data instead of merely inheriting whatever bias happened to be present in a benchmark collection. That setup makes it possible to compare model behavior on “more of the same” versus genuinely novel structural patterns. In other words, the paper is not simply another machine-learning benchmark. It is a stress test for generalization.

The result is sobering but informative. When neural networks are trained on biased datasets, they can perform surprisingly well on held-out sequences that fold into familiar classes of structures. But once the test set contains structures that are outside those familiar patterns, performance drops sharply. The models generalize across sequence variation much more readily than they generalize across structural novelty. That is a warning sign for anyone hoping to use deep learning as a drop-in replacement for biophysical RNA folding models.

An equally important observation is that removing dataset bias does not magically solve the problem. Even on unbiased synthetic data, several architectures struggle to recover basic structural constraints reliably. Some models predict pairing patterns whose scaling with sequence length is simply inconsistent with valid secondary structures. Others produce artifacts that resemble pseudoknots or base triples even when the ViennaRNA-style ground truth does not contain such features at all. These are not minor numerical errors. They point to a mismatch between model output and the combinatorial rules that define the object being predicted.

That is why I still find this article useful years later. It is not an anti-AI paper. It is a paper about technical honesty. If we want machine learning to contribute meaningfully to RNA biology, we need evaluation setups that distinguish memorization from mechanism, and we need models that respect the structural constraints of RNA rather than merely fitting correlations in a benchmark. The work also argues, implicitly, for approaches that combine learning with stronger priors, explicit structure constraints, or experimental information instead of assuming that larger networks alone will fix the problem.

Readers who arrive here from an AI angle may also find it useful to look at some of my other work from the opposite direction. In :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`, I discuss how experimental structure probing can be integrated with computational prediction. In :link-flat:`Conserved RNA regulatory switches in living cells <{filename}/blog/2025-01-01-Conserved-RNA-Regulatory-Switches-in-Living-Cells.rst>`, the focus shifts to transcriptome-scale structural ensembles and experimentally anchored regulatory switches. And if you are more interested in dynamic folding than static structure, :link-flat:`co-transcriptional RNA-ligand interaction dynamics <{filename}/blog/2018-07-01-Efficient_Computation_of_Cotranscriptional_RNA-Ligand_Interaction_Dynamics.rst>` shows the kind of mechanistic modeling that remains hard to replace with black-box prediction alone.

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
