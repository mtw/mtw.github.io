SHAPE directed RNA folding
##########################

:date: 2015-09-02
:modified: 2026-04-24
:tags: ViennaRNA; SHAPE; new method; tools; RNA structure prediction
:category: publications
:slug: SHAPE-directed-RNA-folding
:author: mtw
:summary: This paper shows how SHAPE-guided RNA folding is implemented in the ViennaRNA Package, comparing three widely used strategies for turning nucleotide reactivities into soft constraints that improve thermodynamic structure prediction.
:title: SHAPE directed RNA folding with the ViennaRNA Package
:description: A practical and methodological overview of how SHAPE probing data can be integrated into ViennaRNA to improve RNA secondary structure prediction without abandoning thermodynamic models.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/figures/deigan_method.webp
          :alt: Deigan method adjusts the energetics of stacked base pairs
          :figclass: m-figure m-flat

This paper still gets steady attention, and for good reason. It sits at a practical intersection. People want better RNA structure prediction, they have probing data in hand, and they need a principled way to combine the two. Rather than introducing a wholly new folding formalism, the paper shows how SHAPE reactivities can be fed into the ViennaRNA Package through soft constraints, so experimental evidence can steer prediction without displacing the thermodynamic model underneath.

That is also why the paper has held up so well. Sequence-based folding is often not enough, especially for larger RNAs, regulatory elements, or transcripts with several plausible alternatives. At the same time, probing experiments do not hand over a finished secondary structure. They report on local flexibility and structural context nucleotide by nucleotide. The hard part is turning those measurements into something a folding algorithm can use without pretending the data are exact. This paper is useful because it stays in that narrow but important space between experiment and model.

Methodologically, the paper compares three influential SHAPE-integration strategies and implements them in a common ViennaRNA framework. The Deigan approach converts reactivities into pseudo-energies that act mainly on stacked pairs, which makes it direct and relatively light. The Zarringhalam method reads reactivities in terms of paired and unpaired propensities and spreads penalties more broadly across the structure. The Washietl approach takes a more global view and infers a perturbation of the energy model that reconciles thermodynamic folding with the probing signal while keeping the intervention small. Seeing these methods side by side in one software environment makes their assumptions much easier to compare.

That comparative aspect is one of the strongest features of the paper. It does not argue for one universal recipe. Instead, it shows the choices that matter. How strongly should experimental data push against the default energy model? Is it better to treat reactivities locally, or to interpret them at the ensemble level? What should happen when SHAPE data favor a structure the default parameterization would otherwise underweight? These are the real inference questions behind experiment-guided RNA folding.

The benchmark section matters for the same reason. The paper evaluates the methods on RNAs with known reference structures and looks not only at minimum-free-energy predictions but also at ensemble properties derived from partition function calculations. That broader view is important. SHAPE data do not simply improve one final fold. Very often they sharpen the whole distribution of plausible structures, which makes base-pair probabilities and structural uncertainty more informative. In practice, careful SHAPE-guided folding does better than sequence-only thermodynamic prediction, particularly when several folds are close in free energy.

For many readers, this paper is also a useful introduction to ViennaRNA itself. It shows that the package is more than a set of folding executables. It is a framework in which the energy model can be extended in a controlled way. That software angle explains part of the paper's long life. Published SHAPE datasets can be reanalyzed, methods can be compared under the same machinery, and users are not forced into one opaque implementation.

The paper is also a reminder that some of the best progress in RNA structure prediction comes from combining different kinds of evidence rather than replacing one paradigm with another. Even now, that lesson still holds. Experimental probing, ensemble thinking, and physically interpretable constraints remain central when the goal is biological understanding rather than a better benchmark number.

I discuss the broader issue of experimental confidence in :link-flat:`When to trust RNA structure prediction for experimental decisions <{filename}/blog/2026-03-01-When-to-Trust-RNA-Structure-Prediction-for-Experimental-Decisions.rst>`. This SHAPE paper belongs squarely in that territory, because its value lies in changing which structural hypotheses remain plausible once experimental data are brought in.

For a more direct discussion of what SHAPE and related chemical probing results can and cannot justify in practice, see :link-flat:`How to interpret SHAPE and chemical probing data for RNA structure decisions <{filename}/blog/2026-05-09-How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions.rst>`.

Two useful follow-ups are :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`, which places SHAPE integration into the larger classical RNA-structure field, and :link-flat:`Caveats to deep learning approaches to RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`, which carries the discussion into the later AI period and shows why the underlying inference problem is still harder than many benchmark tables suggest.

For a deeper methodological breakdown, the `Supplementary Data <http://bioinformatics.oxfordjournals.org/content/early/2015/09/23/bioinformatics.btv523/suppl/DC1>`_ remain worth reading. They contain the detailed parameter choices, benchmark setup, and implementation notes behind the SHAPE-directed folding routines.


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
