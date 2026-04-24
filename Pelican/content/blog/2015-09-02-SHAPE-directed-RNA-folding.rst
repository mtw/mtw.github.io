SHAPE directed RNA folding
##########################

:date: 2015-09-02
:modified: 2026-04-24
:tags: ViennaRNA; SHAPE; new method; tools; RNA structure prediction
:category: publications
:slug: SHAPE-directed-RNA-folding
:author: mtw
:summary: This paper brought SHAPE-guided RNA folding into the ViennaRNA Package, comparing three widely used strategies for turning nucleotide reactivities into soft constraints that improve thermodynamic structure prediction.
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

   .. figure:: {static}/files/papers/preview/Preview__Lorenz-2016a.001small.webp
          :alt: Example SHAPE reactivity profile mapped onto an RNA secondary structure
          :figclass: m-figure m-flat

This is one of the papers on this site that still gets steady attention, and for good reason. It sits at a very practical intersection: people want better RNA structure prediction, they have experimental probing data in hand, and they need a principled way to combine the two. That was exactly the problem this paper addressed. Rather than proposing a completely new folding formalism, we showed how SHAPE reactivities could be integrated into the ViennaRNA Package through soft constraints, so that experimental evidence could steer prediction without discarding the thermodynamic model underneath.

That point is worth stressing, because it is the reason the paper aged well. In RNA bioinformatics, purely sequence-based folding is often not enough, especially for larger RNAs, regulatory elements, or molecules with competing structural alternatives. At the same time, probing experiments do not directly hand you the full secondary structure. They provide nucleotide-wise evidence about flexibility and structural context. The real computational challenge is to translate those measurements into something a folding algorithm can use without pretending that the data are exact or noise-free. This paper is attractive to readers because it lives exactly in that middle ground between experiment and model.

Methodologically, the work compared three already influential SHAPE-integration strategies and implemented them in a common ViennaRNA framework. The Deigan approach converts reactivities into pseudo-energies that act mainly on stacked pairs, making it comparatively direct and lightweight. The Zarringhalam method interprets reactivities in terms of paired versus unpaired propensities and distributes penalties more broadly across the structure. The Washietl approach is the most global of the three: it infers a perturbation of the energy model that reconciles thermodynamic folding with the probing signal while trying to keep the intervention as small as possible. Putting these methods side by side in one software environment made it much easier to understand both their similarities and their different modeling assumptions.

That comparative aspect is one of the real strengths of the paper. Instead of presenting a single favored recipe, it gives readers a usable overview of the design space. How aggressively should experimental data override the energy model? Should reactivities be mapped locally to loops, or interpreted more globally at the ensemble level? What happens when SHAPE information supports structures that the default parameterization would otherwise underweight? These are not implementation details in the narrow sense. They are the core inference questions behind experiment-guided RNA folding.

The benchmark section matters for the same reason. We evaluated the methods on RNAs with known reference structures and looked not only at minimum-free-energy predictions but also at ensemble properties derived from partition function calculations. That is important, because SHAPE data often do not just improve a single final fold. They can also sharpen the entire distribution of plausible structures, making base-pair probabilities and structural uncertainty more informative. The practical message was clear: when used carefully, SHAPE-guided folding can outperform sequence-only thermodynamic prediction, especially in cases where alternative structures are close in free energy.

For many readers, this paper is also an accessible entry point into ViennaRNA itself. It shows that the package is not just a collection of folding executables, but a framework in which the energy model can be extended in a controlled way. That software angle helped make the work broadly useful. People could take published SHAPE datasets, use the same computational machinery in their own projects, and compare strategies rather than being locked into a single black-box implementation.

From today's perspective, I think the paper also reads as a reminder that some of the best advances in RNA structure prediction came from integrating heterogeneous evidence rather than from replacing one paradigm with another. Even in the AI era, that lesson still holds. Data-driven methods are useful, but experimental probing, ensemble thinking, and physically interpretable constraints remain central if the goal is biological understanding rather than just a benchmark number.

If this article caught your interest, there are two natural follow-ups on this site. :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>` is the broader review article that places SHAPE integration into the larger classical RNA-structure field. :link-flat:`Caveats to deep learning approaches to RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>` continues the story into the later AI period and explains why the underlying inference problem is still harder than many benchmark tables suggest.

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
