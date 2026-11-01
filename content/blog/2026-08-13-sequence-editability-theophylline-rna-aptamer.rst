Which parts of an RNA aptamer tolerate mutation
###############################################

:date: 2026-08-13
:tags: RNA design; 3D; synthetic biology
:category: publications
:doi: 10.3390/ijms27167228
:paper_title: Computational Analysis of Sequence Editability in the Theophylline RNA Aptamer as a Functional RNA Module
:journal: Int. J. Mol. Sci.
:year: 2026
:paper_license: CC BY 4.0
:paper_authors: Aamir Aman, Leonhard Sidl, Nitchakan Darai, Peter Wolschann, Thanyada Rungrotmongkol, Michael T. Wolfinger
:slug: theophylline-aptamer-sequence-editability
:summary: Molecular dynamics of five theophylline aptamer variants whose binding site is left unchanged: which edits in the surrounding helices keep ligand recognition intact, and which weaken it from the outside.
:title: Sequence editability of the theophylline RNA aptamer
:description: Molecular dynamics of theophylline aptamer variants: which mutations outside the binding pocket keep ligand recognition intact, and which weaken it.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

An RNA aptamer is rarely used on its own. In a designed switch or a sensor it is one module
inside a larger construct, and the rest of the construct has to fold around it: a readout
domain, a competing helix, a spacer. That usually means changing the aptamer sequence,
because the alternative structure one wants to design needs base pairs that the native
sequence does not offer. The nucleotides that touch the ligand are off limits, but they are
a small part of the molecule. This paper asks how much of the rest can be changed, and how
one can decide that before synthesising anything.

The theophylline aptamer is a convenient test case. Its structure in complex with the
ligand has been determined (PDB 8D28), its discrimination against caffeine, which differs
by a single methyl group, is well characterised, and its two outer helices consist
exclusively of G-C pairs. The last point is the practical problem, because a G-C helix is
stable and a competing interaction against it is hard to design. The edits therefore
introduce A-U and G-U pairs: four variants in helix 3 (H3-M1 to H3-M4) and one in helix 1
(H1-M1), which also replaces a non-canonical pair between positions 5 and 29 with a
canonical A-U. None of them changes a nucleotide that contacts the ligand. At the secondary
structure level they cost what one would expect, i.e. the native fold has a free energy of
−13.0 kcal mol⁻¹ and the variants between −9.3 and −11.0 kcal mol⁻¹, while the
:link-flat:`minimum free energy structure <{filename}/glossary.rst#mfe>` stays the same.

Each system was simulated three times for one microsecond with the AMBER OL3 force field,
with the crystallographic Mg²⁺ ions in place, and all analyses use the last 200 ns of each
run. Two controls set the scale for what a disrupted pocket looks like. Removing the Mg²⁺
ions loosens the molecule, i.e. the ligand keeps its contacts but sits in a wider pocket
(solvent-accessible surface 93 Å² instead of 78 Å²). Replacing theophylline with caffeine
is the harsher control: the ligand adopts a rotated orientation, the hydrogen bond to U24
is rarely formed, its surface exposure almost doubles (143 Å²), and in one of the three
runs it leaves the pocket and stays attached to the end of the stem. In the native complex,
by contrast, the U24 contact to the ligand persists at about 3 Å for more than 99 % of the
simulated time, with hydrogen bonds to C22 (99 %), U24 (70 %) and G26 (65 %) and stacking
on C8 (88 %) and A28 (76 %).

Against that scale the five variants separate into two groups. H1-M1 and H3-M3 stay close
to the native aptamer in every measure: backbone stability, per-nucleotide binding energies
(C22, C8 and A28 contribute most, with −3.9, −3.8 and −3.3 kcal mol⁻¹ in the native
complex), the hydrogen-bond and stacking pattern, and the number of ligand contacts.
H3-M2 and H3-M4 weaken the binding signature without touching the binding site: the
acceptor contact shifts from U24 to U23, the stacking occupancies drop, and the ligand
becomes more exposed (105 Å² for H3-M4). H3-M1 is the instructive case in between, because its
mutations clearly destabilise helix 3, where the hydrogen bond occupancies of the edited
pairs fall, and that distortion does not reach the pocket: binding energies, contacts and
the interaction network remain comparable to the native aptamer. A deformed scaffold
therefore does not automatically break recognition, and an untouched binding site does not
guarantee that recognition survives.

Binding free energies were computed with three endpoint methods (MM-GBSA, MM-PBSA and
QM/MM-GBSA) and with the alchemical WaterSwap approach. These methods rest on different
approximations and their absolute values are not comparable with each other, so each
variant was read relative to the native aptamer. The ranking came out the same in all four,
which is the reason to trust it: H3-M3 and H1-M1 with the native, H3-M2 and H3-M4 below it.

A principal component analysis of the six pocket nucleotides puts a number on the
difference. In the native complex the first component accounts for about 19 % of the
variance, i.e. the pocket moves in many small and partly compensating ways. For H3-M4 the
first component accounts for 57 % and for H3-M2 for 65 %, and that dominant motion points
outward at U24 and A28, away from the ligand. The two tolerated variants stay near the
native value (27 % for H1-M1, 30 % for H3-M3), and the Mg²⁺-depleted and caffeine controls
fall in between with inward-directed and rotated motions. A single dominant mode that
displaces the recognition residues is thus a usable marker for an edit that will not work.

What the work provides is a prescreen: a way to sort candidate sequences before they are
made, in a situation where the alternative is to synthesise and measure all of them. Its
requirements are stated explicitly: an experimentally determined structure of the complex
is needed, which exists for the theophylline, neomycin and glutamine aptamers but not for
arbitrary targets, and the edits have to be few enough that the folding pathway is not
re-shaped. The simulations start from the bound state and therefore say nothing about
whether a variant still folds into a binding-competent structure on its own. The
classification into tolerated and disruptive edits is a prediction from simulation, and none
of the five variants has been tested in the laboratory yet.

For the design of ligand-triggered switches this is the step that was usually skipped. The
established workflows either keep the aptamer sequence intact, which limits the alternative
structures one can build around it, or they protect only the binding pocket and assume the
rest is free. The results here say that the rest is not free, but that it is also not
uniformly constrained, and that the difference can be worked out per variant. How the
design objective itself is set up, and why a candidate has to be checked kinetically as
well, is the subject of
:link-flat:`In silico design of ligand-triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>`.

.. frame:: Abstract

   RNA aptamers are often used as ligand-recognition modules in engineered RNA systems, but integration into larger RNA constructs can influence stability and ligand binding. As a result, aptamer sequences may need to be adapted to new environments while preserving essential properties. Here, we examine this sequence editability problem for the theophylline RNA aptamer. Starting from the experimentally determined structure, we introduced targeted mutations in peripheral structural elements while leaving the recognition site unchanged. The native aptamer, mutated variants, a Mg2+-depleted system, and a caffeine-bound control were analyzed using three independent 1 μs molecular dynamics simulations. Binding energetics were estimated with multiple end-point as well as alchemical free energy approaches. Results were interpreted together with base pair stability, the conformational landscape of the binding pocket, and per-nucleotide energy contributions. This allows us to predict whether an edit is tolerated or disruptive. Some mutations retained structural and energetic profiles comparable to the native aptamer, whereas others reduced ligand affinity by propagating structural distortions into the binding pocket. These results show that sequence changes outside the binding site can modulate ligand binding indirectly, and that the ligand interaction network is useful for evaluating edited aptamers. The introduced workflow provides a novel combination of established computational strategies for efficient in silico screening of aptamer variants before experimental testing and can be integrated into the design of larger RNA structures. This works particularly well when an experimental structure is available and the tested mutations are small enough not to disrupt the folding pathway.

Citation
========

  | :link-flat-strong:`Computational Analysis of Sequence Editability in the Theophylline RNA Aptamer as a Functional RNA Module <https://doi.org/10.3390/ijms27167228>`
  | Aamir Aman, Leonhard Sidl, Nitchakan Darai, Peter Wolschann, Thanyada Rungrotmongkol, :ul:`Michael T. Wolfinger`
  | *Int. J. Mol. Sci.* 27(16):7228 (2026) | :doi:`doi:10.3390/ijms27167228 <https://doi.org/10.3390/ijms27167228>` | :link-flat:`Article <https://www.mdpi.com/1422-0067/27/16/7228>`

See also
========

  | :link-flat-strong:`In silico design of ligand triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>`
  | Sven Findeiß, Stefan Hammer, :ul:`Michael T. Wolfinger`, Felix Kühnl, Christoph Flamm, Ivo L. Hofacker
  | *Methods* 143:90-101 (2018) | :doi:`doi:10.1016/j.ymeth.2018.04.003 <https://doi.org/10.1016/j.ymeth.2018.04.003>`

  | :link-flat-strong:`A Structural Refinement Technique for Protein-RNA Complexes Based on a Combination of AI-based Modeling and Flexible Docking: A Study of Musashi-1 Protein <{filename}/blog/2023-06-09-A-Structural-Refinement-Technique-for-Protein-RNA-Complexes-Using-Combination-of-AI-based-Modeling-and-Flexible-Docking-A-Study-of-Musashi-1-Protein.rst>`
  | Nitchakan Darai, Kowit Hengphasatporn, Peter Wolschann, :ul:`Michael T. Wolfinger`, Yasuteru Shigeta, Thanyada Rungrotmongkol, Ryuhei Harada
  | *B. Chem. Soc. Jpn.* 96(7):677–685 (2023) | :doi:`doi:10.1246/bcsj.20230092 <https://doi.org/10.1246/bcsj.20230092>`
