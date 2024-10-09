SHAPE directed RNA folding
##########################

:date: 2015-09-02
:modified: 2024-10-03
:tags: ViennaRNA; SHAPE; new method; tools
:category: publications
:slug: SHAPE-directed-RNA-folding
:author: mtw
:summary: The ViennaRNA Package supports three published approaches for SHAPE-guided RNA structure prediction. Here we evaluate and compare the methods by Deigan, Zarringhalam, and Washietl
:title: SHAPE directed RNA folding with the ViennaRNA Package
:description: In this study we evaluate three published approaches for including SHAPE RNA probing data with the ViennaRNA Package

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi


With the rise of efficient methods for validating RNA structures, particularly through the combination of chemical probing and next-generation sequencing technologies, there has been an increasing need to integrate experimental data, like SHAPE reactivities, with in silico RNA structure prediction tools. These experimental techniques, which provide valuable insights from in vitro or even in vivo conditions, now play a crucial role in enhancing the accuracy of computational RNA structure predictions.

To address this, we recently integrated three established methods for incorporating SHAPE probing data into the ViennaRNA Package. These methods allow experimental data to guide the prediction process, resulting in more accurate RNA structure models. To ensure the effectiveness of these integrations, we rigorously benchmarked the prediction results against a dataset of RNAs with known reference structures, providing a solid validation of the improvements these methods bring to computational RNA structure prediction.

This advancement not only strengthens the predictive power of the ViennaRNA Package, but also bridges the gap between experimental data and computational modeling, allowing researchers to better understand RNA folding and function across diverse biological contexts.

Don't miss the `Supplementary Data <http://bioinformatics.oxfordjournals.org/content/early/2015/09/23/bioinformatics.btv523/suppl/DC1>`_, containing extensive coverage of the applied benchmark strategies and lots of background information.

.. raw:: html

  <object data="{static}/files/papers/Lorenz-2016a.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Lorenz-2016a.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

  Chemical mapping experiments allow for nucleotide resolution
  assessment of RNA structure. We demonstrate that different strategies of
  integrating probing data with thermodynamics-based RNA secondary
  structure prediction algorithms can be implemented by means of soft
  constraints. This amounts to incorporating suitable pseudo-energies into
  the standard energy model for RNA secondary structures. As a showcase
  application for this new feature of the ViennaRNA Package we compare
  three distinct, previously published strategies to utilize SHAPE
  reactivities for structure prediction. The new tool is benchmarked on a
  set of RNAs with known reference structure.

  The capability for SHAPE directed RNA
  folding is part of the upcoming release of the ViennaRNA Package 2.2, for
  which a preliminary release is already freely available at
  http://www.tbi.univie.ac.at/RNA.


Citation
========

  | :link-flat-strong:`SHAPE directed RNA folding <http://bioinformatics.oxfordjournals.org/content/early/2015/09/23/bioinformatics.btv523.abstract>`
  | Ronny Lorenz, Dominik Luntzer, Ivo L. Hofacker, Peter F. Stadler, Michael T. Wolfinger
  | *Bioinformatics* 32: 145–47 (2016) | :doi:`doi:10.1093/bioinformatics/btv523 <https://doi.org/10.1093/bioinformatics/btv523>` | :link-flat:`PDF <{static}/files/papers/Lorenz-2016a.pdf>`


See also
========

  | :link-flat-strong:`Predicting RNA Structures from Sequence and Probing Data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`
  | Ronny Lorenz, :ul:`Michael T. Wolfinger`, Andrea Tanzer, Ivo L. Hofacker
  | *Methods* 103:86–98 (2016) | :doi:`doi:10.1016/j.ymeth.2016.04.004 <https://doi.org/10.1016/j.ymeth.2016.04.004>` | :link-flat:`PDF <{static}/files/papers/Lorenz-2016.pdf>`


..
  .. block-info:: Citations

      .. container:: m-label

          .. raw:: html

            <span class="__dimensions_badge_embed__" data-doi="10.1093/bioinformatics/btv523" data-style="small_rectangle"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>

      .. container:: m-label

          .. raw:: html

            <script type="text/javascript" src="https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"></script><div class="altmetric-embed" data-badge-type="2" data-badge-popover="bottom" data-doi="10.1093/bioinformatics/btv523"></div>
