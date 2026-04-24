Folding Kinetics of Large RNAs
##############################

:date: 2008-06-01
:modified: 2026-04-24
:tags: RNA folding kinetics; co-transcriptional RNA folding
:category: publications
:slug: folding-kinetics-of-large-rnas
:author: mtw
:summary: Kinwalker predicts folding trajectories of large RNAs by combining locally optimal substructures and kinetic heuristics, making co-transcriptional folding analysis feasible for molecules up to about 1500 nucleotides.
:title: Folding kinetics of large RNAs
:description: A heuristic approach to RNA folding kinetics that enables co-transcriptional folding predictions for much longer sequences than earlier methods.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Classical RNA folding kinetics methods become difficult to scale once sequences move beyond the size range of small regulatory RNAs. This paper addresses that limitation with Kinwalker, a heuristic that predicts folding trajectories by combining locally optimal substructures rather than trying to explore the full kinetic landscape explicitly.

The algorithm starts from a simple but powerful observation: many important metastable intermediates appear to be composed of locally favorable structural building blocks. Kinwalker therefore precomputes thermodynamically optimal local structures by dynamic programming, then assembles them stepwise into a global folding trajectory while resolving conflicts between overlapping alternatives. Folding events are interleaved with transcription events, which makes the method particularly suitable for co-transcriptional folding problems.

That design gives the method a very different operating regime from exhaustive simulation. Instead of aiming for exact kinetics on all possible paths, it attempts to recover the dominant trajectory structure for much larger RNAs than earlier methods could handle. The paper reports applicability to sequences of roughly 1500 nucleotides, which was a substantial extension at the time and made many biologically relevant systems computationally accessible.

The validation examples are important here. Kinwalker reproduces several experimentally studied folding scenarios, including delayed cloverleaf formation in bacteriophage RNAs, the ASR riboswitch, and the Hok system. These are exactly the kinds of RNAs where kinetic and co-transcriptional effects matter more than the equilibrium minimum free energy structure alone. In that sense, the paper is not just a scaling story; it is also a strong argument that useful kinetic prediction can come from carefully chosen heuristics when full landscape exploration is infeasible.

For the site’s core topics, this paper belongs squarely in the `RNA folding kinetics` and `co-transcriptional RNA folding` cluster. It remains a useful reference point for anyone interested in how to bridge thermodynamic RNA structure prediction with folding-pathway analysis for longer molecules.

.. frame:: Abstract

   We introduce here a heuristic approach to kinetic RNA folding that constructs secondary structures by stepwise combination of building blocks. These blocks correspond to sub-sequences and their thermodynamically optimal structures. These are determined by the standard dynamic programming approach to RNA folding. Folding trajectories are modeled at base pair resolution using the Morgan-Higgs heuristic and a barrier tree based heuristic to connect combinations of the local building blocks. Implemented in the program Kinwalker, the algorithm allows co-transcriptional folding and can be used to fold sequences of up to about 1500 nucleotides in length. A detailed comparison with several well-studied examples from the literature, including the delayed folding of bacteriophage cloverleaf structures, the ASR riboswitch, and the Hok RNA, shows an excellent agreement of predicted trajectories and experimental evidence. The software is available as part of the Vienna RNA Package.

Citation
========

  | :link-flat-strong:`Folding Kinetics of Large RNAs <{filename}/blog/2008-06-01-Folding-Kinetics-of-Large-RNAs.rst>`
  | Michael Geis, Christoph Flamm, :ul:`Michael T. Wolfinger`, Andrea Tanzer, Ivo L. Hofacker, Martin Middendorf, Christian Mandl, Peter F. Stadler, Caroline Thurner
  | *J. Mol. Biol.* 379(1):160–173 (2008) | :doi:`doi:10.1016/j.jmb.2008.02.064 <https://doi.org/10.1016/j.jmb.2008.02.064>` | :link-flat:`Preprint PDF <{static}/files/papers/Geis-2008__PREPRINT.pdf>`

