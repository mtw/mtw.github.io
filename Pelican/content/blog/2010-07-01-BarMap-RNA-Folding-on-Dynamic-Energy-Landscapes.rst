BarMap: RNA Folding on Dynamic Energy Landscapes
################################################

:date: 2010-07-01
:modified: 2026-04-24
:tags: co-transcriptional RNA folding; RNA folding kinetics; energy landscapes
:category: publications
:slug: barmap-rna-folding-dynamic-energy-landscapes
:author: mtw
:summary: BarMap models RNA folding on changing energy landscapes by linking macrostates between landscape snapshots, enabling efficient analysis of co-transcriptional and externally perturbed folding scenarios.
:title: BarMap and RNA folding on dynamic energy landscapes
:description: A coarse-grained approach to RNA folding kinetics on changing landscapes, including co-transcriptional folding and other nonstationary scenarios.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

RNA folding rarely happens on a fixed energy landscape. During transcription, degradation, ligand binding, or temperature shifts, the available structure space changes over time, and with it the kinetic pathways. This paper addresses exactly that nonstationary setting by extending landscape-based RNA kinetics from a single static landscape to a sequence of related landscapes connected through time.

The central idea of BarMap is to treat each time point or perturbation step as a snapshot landscape with its own macrostates, and then define a mapping between neighboring snapshots. Population densities can then be transferred from one coarse-grained landscape to the next instead of starting the kinetics calculation from scratch each time. In effect, the expensive landscape analysis becomes a preprocessing step, while the temporal evolution is handled by moving populations across linked barrier-tree representations.

That is a particularly natural fit for co-transcriptional folding, where the RNA chain grows one nucleotide at a time and each elongation step slightly reshapes the landscape. But the same formalism also applies to temperature changes, refolding after cleavage, and mechanically constrained scenarios. The paper therefore broadens the energy-landscape view of RNA folding kinetics into a framework for dynamic landscapes, which is much closer to the situations encountered by regulatory RNAs in cells.

From a methodological perspective, this is a useful complement to trajectory-based simulators. It does not aim to reconstruct every folding path explicitly. Instead, it keeps the coarse-grained view at the level of basins, barriers, and saddle points, while allowing those basins themselves to change over time. That makes it possible to study larger and more complex nonstationary folding scenarios than a direct simulation strategy would usually permit.

BarMap is therefore one of the key papers in the `co-transcriptional RNA folding` and `RNA folding kinetics` cluster. It formalizes the idea that kinetics should often be thought of as motion across a sequence of changing landscapes, not just as diffusion on a single fixed one.

.. frame:: Abstract

   Dynamical changes of RNA secondary structures play an important role in the function of many regulatory RNAs. Such kinetic effects, especially in time-variable and externally triggered systems, are usually investigated by means of extensive and expensive simulations of large sets of individual folding trajectories. Here we describe the theoretical foundations of a generic approach that not only allows the direct computation of approximate population densities but also reduces the efforts required to analyze the folding energy landscapes to a one-time preprocessing step. The basic idea is to consider the kinetics on individual landscapes and to model external triggers and environmental changes as small but discrete changes in the landscapes. A ‘‘barmap’’ links macrostates of temporally adjacent landscapes and defines the transfer of population densities from one ‘‘snapshot’’ to the next. Implemented in the BarMap software, this approach makes it feasible to study folding processes at the level of basins, saddle points, and barriers for many nonstationary scenarios, including temperature changes, cotranscriptional folding, refolding in consequence to degradation, and mechanically constrained kinetics, as in the case of the translocation of a polymer through a pore.

Citation
========

  | :link-flat-strong:`BarMap: RNA Folding on Dynamic Energy Landscapes <{filename}/blog/2010-07-01-BarMap-RNA-Folding-on-Dynamic-Energy-Landscapes.rst>`
  | Ivo L. Hofacker, Christoph Flamm, Christian Heine, :ul:`Michael T. Wolfinger`, Gerik Scheuermann, Peter F. Stadler
  | *RNA* 16:1308–1316 (2010) | :doi:`doi:10.1261/rna.2093310 <https://doi.org/10.1261/rna.2093310>` | :link-flat:`PDF <{static}/files/papers/Hofacker-2010.pdf>`

