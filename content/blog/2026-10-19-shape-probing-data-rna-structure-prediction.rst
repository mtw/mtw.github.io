SHAPE and chemical probing data in RNA structure prediction
###########################################################

:date: 2026-10-19
:tags: ViennaRNA; SHAPE; RNA structure prediction; tools
:category: howto
:section: guides
:slug: How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions
:title: SHAPE and chemical probing data in RNA structure prediction: how to fold with reactivities in ViennaRNA
:summary: How SHAPE reactivities go into RNAfold, what the three methods in ViennaRNA do with them, and what probing data change in a prediction and what they do not. Worked example with yeast tRNA-Phe, all commands included.
:description: How to use SHAPE and chemical probing reactivities in RNAfold: the input format, the Deigan, Zarringhalam and Washietl methods, and what the data change.

.. role:: link-flat(link)
  :class: m-flat m-text

Chemical probing experiments such as SHAPE give you one number per nucleotide, and the
question I get asked most often about them is how these numbers go into RNAfold and what
they actually do to a prediction. This post is a hands-on answer. I use yeast tRNA-Phe as
the example because everybody knows the cloverleaf, and I go through the three ways
ViennaRNA has to fold with probing data. All commands were run with ViennaRNA 2.7.2, and
copy and paste should reproduce every output shown here.

What SHAPE measures
-------------------

SHAPE (selective 2'-hydroxyl acylation analyzed by primer extension) uses a reagent that
modifies the 2'-OH of flexible nucleotides. Nucleotides in a helix are modified rarely,
nucleotides in loops, bulges and unstructured regions more often. Reverse transcription
stops at the modified positions, and counting the stops gives a reactivity for every
nucleotide, usually normalized such that most values fall between 0 and about 2.

Two things about these numbers are important. A reactivity is not a pairing state. A low
value means the nucleotide is constrained somehow, not that it pairs with a particular
partner; a high value means flexible, which is true for unpaired bases but also for bases
in weak or dynamic pairs and at helix ends. And the values are noisy, with a scale that
depends on the experiment. For these reasons ViennaRNA does not use reactivities to fix
base pairs. It uses them to modify the energy model, as soft constraints, and the three
methods implemented in RNAfold differ in how exactly they do that.

The example and the starting point
----------------------------------

Put the sequence of yeast tRNA-Phe in a FASTA file ``tRNA.fa``:

.. code-block:: text

   >tRNA-Phe
   GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA

``RNAfold -p`` gives the MFE structure together with the ensemble properties:

.. code-block:: bash

   RNAfold -p --noPS < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-22.40)
   (((((({...,(({{{{,({.,,,,.||,||}}},.,.||||..||||,,{{{...,,}}}})))))))))).... [-24.13]
   (((((((.....(((................)))...............................))))))).... { -3.01 d=16.21}
    frequency of mfe structure in ensemble 0.060652; ensemble diversity 23.38

The first line is the MFE structure, the cloverleaf. The second line gives the ensemble
free energy, with symbols that code the pair probabilities. The third line is the centroid
structure, here with three base pairs. The last line says that the MFE structure has a
frequency of only 6% in the Boltzmann ensemble, and an ensemble diversity of 23 is huge
for a 76 nt RNA. In other words, the energy model considers lots of alternatives nearly
as good as the cloverleaf, and this is exactly the situation where probing data help.
Note that ``-p`` also writes the dot plot ``tRNA-Phe_dp.ps`` with all pair probabilities;
``--noPS`` only suppresses the structure drawing. I will use the dot plot below.

The input format
----------------

RNAfold expects one line per nucleotide with position (1-based), nucleotide and
reactivity:

.. code-block:: text

   1 G 0.15
   2 C 0.24
   3 G 0.24
   4 G 0.05
   5 A 0.13
   ...

Positions without data can be omitted; RNAfold then simply has no information for them.
Whatever your probing pipeline produces, a few lines of ``awk`` bring it into this form.

A word on the data used here. I do not have a SHAPE profile for this particular sequence,
and this post is about the mechanics, not about a specific experiment. The profile I use
is therefore synthetic: I took the known cloverleaf and assigned uniformly random
reactivities between 0.7 and 1.6 to unpaired positions and between 0 and 0.25 to paired
positions. Real data are noisier, in particular at helix ends. The behavior of the
programs is the same for real data, the numbers are not. The file is
:link-flat:`tRNA-Phe.shape <{static}/files/tutorials/tRNA-Phe.shape>`; save it as
``tRNA.shape`` to run the commands below.

Method D (Deigan): pseudo-energies for stacked pairs
----------------------------------------------------

.. code-block:: bash

   RNAfold --noPS --shape=tRNA.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-48.64)

This is the default method. Each reactivity *r* is converted into a pseudo-energy
ΔG(r) = m · ln(r + 1) + b with m = 1.8 and b = −0.6 kcal/mol (Deigan et al. 2009), and
this term is added for every nucleotide that is part of a stacked pair. Low reactivities
give a negative contribution, i.e. a bonus for pairing, high reactivities a penalty. The
recursions of the folding algorithm stay the same, only the energies change.

Note that the energy printed, −48.64, is not a free energy anymore. It contains the
pseudo-energies and must not be compared with the −22.40 of the unconstrained prediction.
The structure is the same cloverleaf as before, so the data did not change the MFE
prediction at all. What they did change becomes visible with the partition function:

.. code-block:: bash

   RNAfold -p --noPS --shape=tRNA.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-48.64)
   (((((((..((((........)))).(((((.....,.))))).....(((((.......)))))))))))).... [-49.07]
   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... {-48.64 d=0.56}
    frequency of mfe structure in ensemble 0.49869; ensemble diversity 0.88

Before: MFE frequency 0.06, diversity 23.4, a centroid with three pairs. After: MFE
frequency 0.50, diversity 0.88, and the centroid is the cloverleaf. In the dot plot, 20 of
the 21 cloverleaf pairs now have a probability above 0.98; the one exception is 49-65,
the closing pair of the T stem next to the multiloop, at 0.97. So the data did not move
the prediction, they removed the alternatives.

Slope and intercept can be changed, e.g. ``--shapeMethod="Dm1.9b-0.7"``, or individually
(``"Dm1.9"``, ``"Db-0.7"``). A larger slope gives the data more weight relative to the
energy model. I would leave the defaults alone unless you have calibrated your own
experiment. They were fitted for normalized reactivities on a 0–2 scale; data on a
different scale should be rescaled, not compensated with m.

Method Z (Zarringhalam): penalize deviations from the data
----------------------------------------------------------

.. code-block:: bash

   RNAfold --noPS --shape=tRNA.shape --shapeMethod=Z < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-14.30)

Here the reactivities are first converted into probabilities of being unpaired, and the
recursion is penalized for every nucleotide whose predicted state deviates from that
probability. The weight of the penalty is β, default 0.89, set with
``--shapeMethod="Zb0.8"``. The conversion from reactivity to probability is selected with
``--shapeConversion``: the default ``O`` fits a linear model to the log reactivities,
``C0.25`` calls everything above 0.25 unpaired, and ``S`` skips the conversion if the
file already contains unpaired probabilities. For our profile the result is again the
cloverleaf, with an energy that includes penalty terms and is not a free energy. With
``-p``, the MFE frequency is 0.88 and the diversity 0.27, i.e. on this clean profile Z
narrows the ensemble even more than D.

Method W (Washietl): a perturbation vector
------------------------------------------

W works differently. It does not convert reactivities on the fly but expects a
*perturbation vector*, a small energy correction per nucleotide, chosen such that the
predicted unpaired probabilities match the data as well as possible while the energy
model is changed as little as possible. This vector is computed with ``RNApvmin``, which
solves the corresponding optimization problem (progress goes to stderr, the vector to
stdout):

.. code-block:: bash

   RNApvmin tRNA.shape < tRNA.fa > tRNA.pv
   RNAfold --noPS --shape=tRNA.pv --shapeMethod=W < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-24.44)

For our profile the corrections are between about −0.2 and +0.15 kcal/mol, most of them
much smaller, and RNAfold gives the cloverleaf with an energy close to the thermodynamic
one. The minimization in ``RNApvmin`` does not end in exactly the same vector on repeated
runs, so expect the second decimal to differ; in three runs I got −24.44 to −24.55. With
``-p`` the MFE frequency is about 0.33 and the diversity between 8 and 9, so W is the
least invasive of the three methods here. If you pass raw reactivities to ``--shapeMethod=W`` by
mistake, RNAfold reads them as energies and the result is garbage. The structure then has
nothing to do with the data, which makes the error easy to spot.

Which method? D is the default, the fastest and the most widely used. Z and W are useful
to see how much the result depends on the way the data enter the model. If all three
agree, the conclusion does not depend on this choice. If they disagree, the data are not
decisive for that region.

What the data change, and what they do not
------------------------------------------

Three small experiments show what probing data do and what they do not do.

**Partial data.** Assume only the anticodon loop, positions 32–38, was probed:

.. code-block:: bash

   awk '$1>=32 && $1<=38' tRNA.shape > partial.shape
   RNAfold --noPS --shape=partial.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-22.40)

Nothing changes, and the energy is the thermodynamic one: the data agree with the MFE
structure at these positions, and no other position got a pseudo-energy term. Probing
data act only where they exist, and only where they contradict the model.

**Contradicting data.** Now set the reactivities of positions 1–7, the 5' side of the
acceptor stem, to 1.2, as if these nucleotides had been found flexible:

.. code-block:: bash

   awk '{ if ($1<=7) printf "%d %s 1.20\n", $1, $2; else print }' tRNA.shape > contra.shape
   RNAfold -p --noPS --shape=contra.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-34.29)
   (((({{...((((........)))).(((((.....,.))))).....(((((.......))))),}})))).... [-35.46]
   ((((((...((((........)))).(((((.......))))).....(((((.......))))).)))))).... {-34.07 d=2.18}
    frequency of mfe structure in ensemble 0.149346; ensemble diversity 3.04

The MFE structure is still the cloverleaf. A penalty of about 0.8 kcal/mol for every
stack one of the nucleotides 1–7 takes part in is not enough to break a stem of seven
pairs, three of them GC. The ensemble, however, has
changed a lot: the MFE frequency drops from 0.50 to 0.15, the diversity rises from 0.88
to 3.0, and the centroid has lost the pair 7-66. In the dot plot the acceptor stem pairs
now have probabilities of 0.96, 0.97, 0.93, 0.73, 0.64, 0.53 and 0.31 from the outside
in, down from 0.99 or better; the three other stems stay at 1.00. ``RNAsubopt`` shows the
alternatives the data have pulled up:

.. code-block:: bash

   RNAsubopt -e 0.5 --shape=contra.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   >tRNA-Phe [50]
   GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA -34.29   0.50
   (((......((((........)))).(((((.......))))).....(((((.......)))))....))).... -33.95
   ((((((...((((........)))).(((((.......))))).....(((((.......))))).)))))).... -34.07
   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... -34.29
   (((((((..((((........)))).((((((....).))))).....(((((.......)))))))))))).... -33.99

A structure with only the three GC pairs of the acceptor stem is 0.34 kcal/mol above the
optimum; without the data it is 3.5 kcal/mol above. This is what soft constraints are:
data and energy model pull in different directions, and the result is a shift in
probabilities before it is a different structure. If you look at the MFE structure alone
you miss this completely. A larger slope, ``--shapeMethod="Dm2.6b-0.8"``, removes the
acceptor stem from the MFE structure altogether. If you want to force positions to be
unpaired, use hard constraints (``RNAfold -C``), which is a different question.

**Consistent data.** This is the case shown above with the full profile, and the common
case with good data on a well-folded RNA: the structure stays, the alternatives disappear
from the ensemble. Instead of "the MFE structure with 6% support" you get "the MFE
structure with half the ensemble behind it and 20 of 21 pairs above 0.98". That is a
statement you can base an experiment on.

Practical notes
---------------

- Normalize reactivities before use (the usual 2–8% rule, or whatever your pipeline
  does) and look at the distribution. A profile with almost all values near zero, or with
  a long tail above 3, tells you something about the experiment rather than the RNA.
- Reactivities measured in cells report on the RNA in its cellular context, with bound
  proteins, ribosomes and ions. Folding such data with a model of the naked RNA is
  legitimate, but the result describes what a protein-free RNA with these constraints
  would do, not the structure in the cell.
- Always run the partition function with the data. The MFE structure alone hides the
  main effect, which is on the probabilities.
- Report which method and parameters you used. The energies are not comparable across
  methods or with unconstrained folding.
- Keep the comparison to the unconstrained prediction. The regions where the data changed
  the structure are the regions where the thermodynamic model was uncertain. These are
  also the regions where your conclusion rests on the experiment, and where a second
  experiment is most informative.

Further reading
---------------

- Lorenz R, Luntzer D, Hofacker IL, Stadler PF, Wolfinger MT. SHAPE directed RNA folding.
  *Bioinformatics* 32:145–147 (2016). doi:10.1093/bioinformatics/btv523. The
  implementation of the three methods in ViennaRNA and their comparison; on this site:
  :link-flat:`SHAPE directed RNA folding <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>`.
- Lorenz R, Wolfinger MT, Tanzer A, Hofacker IL. Predicting RNA secondary structures from
  sequence and probing data. *Methods* 103:86–98 (2016). doi:10.1016/j.ymeth.2016.04.004;
  on this site: :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`.
- Deigan KE, Li TW, Mathews DH, Weeks KM. Accurate SHAPE-directed RNA structure
  determination. *Proc Natl Acad Sci USA* 106:97–102 (2009).
- Zarringhalam K, Meyer MM, Dotu I, Chuang JH, Clote P. Integrating chemical footprinting
  data into RNA secondary structure prediction. *PLoS ONE* 7:e45160 (2012).
- Washietl S, Hofacker IL, Stadler PF, Kellis M. RNA folding with soft constraints:
  reconciliation of probing data and thermodynamic secondary structure prediction.
  *Nucleic Acids Res* 40:4261–4272 (2012).
