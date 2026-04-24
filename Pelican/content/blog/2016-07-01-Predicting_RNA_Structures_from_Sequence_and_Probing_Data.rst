Predicting RNA Structures from Sequence and Probing Data
########################################################

:date: 2016-07-01
:modified: 2026-04-24
:tags: ViennaRNA; RNA design; RNA folding kinetics; SHAPE; RNA structure conservation; RNA structure prediction
:category: publications
:slug: Predicting-RNA-Structures-from-Sequence-and-Probing-Data
:author: mtw
:summary: This review explains how classical thermodynamic RNA folding models can be improved with chemical probing data, and why that combination remains one of the most reliable routes to biologically useful structure prediction.
:title: Predicting RNA structures from sequence and probing data
:description: A review of classical RNA secondary structure prediction, ensemble-based folding, and the integration of SHAPE and related probing data into thermodynamic models.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

RNA secondary structure prediction is sometimes presented as if there were a clean historical break between “old biophysics” and “new AI”. In practice, that is not how the field developed. Long before the current machine-learning wave, RNA bioinformatics had already built a sophisticated toolkit around thermodynamic folding, ensemble analysis, comparative evidence, and experimental structure probing. This review was written in that pre-AI period, and that is precisely why it is still useful: it explains the core logic of the field without mistaking benchmark performance for mechanistic understanding.

The starting point is the classical thermodynamic view of RNA folding. Dynamic programming algorithms can efficiently compute minimum-free-energy structures, base-pairing probabilities, and partition-function ensembles under a well-defined energy model. These methods remain powerful because they do more than output a single structure. They provide an explicit physical interpretation of structural alternatives, uncertainty, and energetic tradeoffs. The review therefore emphasizes that RNA structure prediction should not be reduced to “find the one correct fold”. For many RNAs, the ensemble itself is the relevant biological object.

At the same time, purely sequence-based thermodynamic prediction has obvious limits. Energy parameters are imperfect, tertiary interactions are usually treated only indirectly, and the energetically optimal structure is not always the biologically realized one. This becomes especially clear for regulatory RNAs, long transcripts, and systems shaped by kinetics, ligand binding, proteins, or cellular context. The review lays out these limitations clearly, which is one reason it has remained a useful reference.

The main contribution of the article is its overview of how chemical and enzymatic structure probing can be integrated with folding algorithms. Methods such as SHAPE, PARS, and related probing strategies provide nucleotide-resolution information about local flexibility or accessibility. The important computational question is how to convert such experimental readouts into something a folding algorithm can use. The review discusses approaches based on pseudo-energies and soft constraints, where probing reactivities perturb the thermodynamic model rather than replacing it outright. That design choice matters: it allows the prediction to stay grounded in base-pairing energetics while still being steered by experimental evidence.

This combination of experiment and computation was, and remains, one of the most productive ideas in RNA structure prediction. Probing data can help discriminate among near-optimal folds, recover structures that sequence-only models miss, and improve the interpretation of structural ensembles. But the review is careful not to oversell the approach. Experimental data are noisy, condition-dependent, and often indirect. A reactivity profile is not itself a structure. It still has to be interpreted through a model, and the quality of the result depends on both the experiment and the computational framework used to incorporate it.

That balanced perspective is what makes the article age well. It is optimistic about integrating data with theory, but it does not pretend that more data automatically solve the inference problem. In that sense, the paper anticipated a lesson that remains relevant in the AI era as well: prediction gets better when models encode the right constraints and when external evidence is incorporated thoughtfully, not when we simply add another layer of complexity.

For readers new to the topic, this review is a good entry point because it connects several levels of the field at once: classical RNA folding algorithms, ensemble thinking, experimental probing, and practical strategies for combining them. For readers already working in RNA biology, it remains a strong reminder that the most reliable structural insight often comes from combining complementary sources of information rather than choosing between “physics” and “data”.

If this topic is of interest, there are two natural follow-ups on this site. :link-flat:`SHAPE directed RNA folding with the ViennaRNA Package <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>` is the more implementation-focused companion piece, describing specific SHAPE integration strategies in ViennaRNA. :link-flat:`Caveats in deep learning for RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>` picks up the story from the later AI period and explains why data-driven models still benefit from the classical structural thinking summarized here.

.. frame:: Abstract

  RNA secondary structures have proven essential for understanding the regulatory functions performed by RNA such as microRNAs, bacterial small RNAs, or riboswitches. This success is in part due to the availability of efficient computational methods for predicting RNA secondary structures. Recent advances focus on dealing with the inherent uncertainty of prediction by considering the ensemble of possible structures rather than the single most stable one. Moreover, the advent of high-throughput structural probing has spurred the development of computational methods that incorporate such experimental data as auxiliary information.

Citation
========

  | :link-flat-strong:`Predicting RNA Structures from Sequence and Probing Data <https://doi.org/10.1016/j.ymeth.2016.04.004>`
  | Ronny Lorenz, :ul:`Michael T. Wolfinger`, Andrea Tanzer, Ivo L. Hofacker
  | *Methods* 103:86–98 (2016) | :doi:`doi:10.1016/j.ymeth.2016.04.004 <https://doi.org/10.1016/j.ymeth.2016.04.004>` | :link-flat:`PDF <{static}/files/papers/Lorenz-2016.pdf>`

See Also
========

  | :link-flat-strong:`SHAPE Directed RNA Folding <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>`
  | Ronny Lorenz, Dominik Luntzer, Ivo L. Hofacker, Peter F. Stadler, :ul:`Michael T. Wolfinger`
  | *Bioinformatics* 32: 145–47 (2016) | :doi:`doi:10.1093/bioinformatics/btv523 <https://doi.org/10.1093/bioinformatics/btv523>` | :link-flat:`PDF <{static}/files/papers/Lorenz-2016a.pdf>`
