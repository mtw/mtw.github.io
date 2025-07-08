SHAPE directed RNA folding
##########################

:date: 2015-09-02
:modified: 2025-07-08
:tags: ViennaRNA; SHAPE; new method; tools
:category: publications
:slug: SHAPE-directed-RNA-folding
:author: mtw
:summary: The ViennaRNA Package 2.0 brings powerful dynamic programming algorithms to researchers studying nucleic acid folding. In this post, we explore three SHAPE-guided methods—Deigan, Zarringhalam, and Washietl—that have been integrated into our toolkit to improve predictions of base pair interactions and minimum free energy (MFE) structures for RNA molecules. By combining chemical probing data with in silico modeling, these approaches help capture real-world folding behaviors and enhance the accuracy of computational RNA structure predictions
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

Bridging Experiment with Computation
++++++++++++++++++++++++++++++++++++

Modern experiments generate SHAPE reactivity profiles through selective 2’-hydroxyl acylation analyzed by primer extension, a method that reveals nucleotide flexibility in vitro or in vivo. To translate these reactivities into structural guidance, the Deigan, Zarringhalam, and Washietl methods each adjust the energy parameters used in traditional dynamic programming: Deigan’s model applies pseudo-energies directly to loops, Zarringhalam’s method uses reactivity-specific weights, and Washietl’s approach infers perturbation of the energy parameters to optimally fit the SHAPE signal. Together, these innovations allow the prediction of both the minimum free energy (MFE) structure and the ensemble of probable folds with improved sensitivity to experimental data.

Performance and Benchmarking
++++++++++++++++++++++++++++

To validate these implementations, we benchmarked against a curated set of RNAs with known reference structures, analyzing metrics like sensitivity and positive predictive value for predicted base pairs. The comparisons covered both the MFE structure and the full partition function ensemble, demonstrating that SHAPE-guided predictions outperform purely thermodynamic models, especially for challenging motifs. Detailed supplementary data outline our benchmark strategies, energy parameter settings, and the impact on diverse RNA molecules, confirming the value of integrating experimental evidence into computational pipelines.

Getting Started: Command Line and Source Code
+++++++++++++++++++++++++++++++++++++++++++++

Users can install binary packages for several Linux distributions or build from source code available on our repository. The command line interface supports  commands for folding, partition function calculation, and SHAPE-guided modes, with options to specify and adjust energy parameters directly. Whether you’re scripting large-scale screens or running individual analyses, our tools and comprehensive documentation provide everything needed to apply dynamic programming algorithms to your nucleic acid research.

For a deep dive, don’t miss the `Supplementary Data <http://bioinformatics.oxfordjournals.org/content/early/2015/09/23/bioinformatics.btv523/suppl/DC1>`_, which includes extensive background on each method, parameter details, and full benchmark results for our SHAPE-integrated algorithms. Dive into the code, explore the options, and see how experimental data can guide your next discovery in RNA structure prediction.


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
