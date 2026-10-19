SHAPE and chemical probing data in RNA structure prediction
###########################################################

:date: 2026-10-19
:tags: ViennaRNA; SHAPE; RNA structure prediction; tools
:category: howto
:section: guides
:slug: How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions
:title: SHAPE and chemical probing data in RNA structure prediction: how to fold with reactivities in ViennaRNA
:summary: Chemical probing reports on nucleotide flexibility, not on base pairs. This tutorial shows how SHAPE reactivities enter RNAfold as soft constraints, what the three methods in ViennaRNA do with them, and, on a yeast tRNA as the worked example, what the data change in a prediction and what they leave alone.
:description: How to use SHAPE and chemical probing reactivities in RNAfold: the input format, the Deigan, Zarringhalam and Washietl methods, and what the data change.

.. role:: link-flat(link)
  :class: m-flat m-text

For yeast tRNA-Phe, RNAfold's minimum free energy structure is the correct cloverleaf, but
the thermodynamic model gives that structure only six percent of the Boltzmann ensemble.
The model is missing information, and chemical probing supplies some of it. This post
shows how SHAPE reactivities are given to RNAfold, what the three available methods do
with them, and, the part that matters most in practice, what the data change and what they
leave as they were. All outputs are from ViennaRNA 2.7.2.

What SHAPE measures
-------------------

SHAPE (selective 2′-hydroxyl acylation analysed by primer extension) treats the RNA with a
reagent that reacts with the 2′-OH of flexible nucleotides. Nucleotides held in a helix
react little; nucleotides in loops, bulges and unstructured regions react more. Reading the
reaction sites out by reverse transcription gives one number per nucleotide, the
reactivity, usually normalised so that most values lie between 0 and about 2. DMS and
other probing chemistries deliver the same kind of per-nucleotide profile and enter RNAfold
the same way.

Two properties of these numbers decide how they should be used. First, a reactivity is not
a pairing state: a low value says "probably constrained", not "paired with position j"; a
high value says "flexible", which includes unpaired bases, bases in weak or dynamic pairs,
and some bases at helix ends. Second, the values are noisy and their scale depends on the
experiment. So the data are best used to *shift* the energy model rather than to dictate
pairs. That is what all three methods in ViennaRNA do; they differ in how the shift is
computed.

The sequence and the baseline
-----------------------------

.. code-block:: text

   >tRNA-Phe
   GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA

Save this as ``tRNA.fa``. Without data, ``RNAfold -p`` gives the cloverleaf as the minimum
free energy (MFE) structure and shows how weakly the model supports it:

.. code-block:: bash

   RNAfold -p --noPS < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-22.40)
   (((((((.....(((................)))...............................))))))).... { -3.01 d=16.21}
    frequency of mfe structure in ensemble 0.060652; ensemble diversity 23.38

The first line is the MFE structure, the second the centroid of the ensemble (with its
mean base-pair distance to the ensemble), the third the share of the ensemble the MFE
structure has and the ensemble diversity. A frequency of 0.06 and a centroid with three
pairs mean that the model considers many alternative folds almost as good as the
cloverleaf. ``-p`` also writes ``tRNA-Phe_dp.ps``, the dot plot with every pair
probability.

The input file
--------------

One line per nucleotide: position (1-based), the nucleotide, the reactivity.

.. code-block:: text

   1 G 0.15
   2 C 0.24
   3 G 0.24
   4 G 0.05
   5 A 0.13
   ...

Positions without a measurement can be left out; RNAfold treats them as having no data.
Most probing pipelines (ShapeMapper, RNAFramework, QuShape) write this format or
something a one-line ``awk`` turns into it.

**About the data in this post.** I do not have a SHAPE profile for this exact sequence at
hand, and the point of the post is the mechanics, so the profile used below is
*illustrative*: it was generated from the known cloverleaf by giving unpaired positions
uniformly random reactivities between 0.7 and 1.6 and paired positions values between 0
and 0.25. Real data are noisier and less clean at helix ends. Everything the commands show
about how the program behaves holds for real data; the specific numbers do not. The file
is :link-flat:`tRNA-Phe.shape <{static}/files/tutorials/tRNA-Phe.shape>` if you want to
run the commands as they stand; save it as ``tRNA.shape``.

Method D (Deigan): a per-nucleotide energy bonus or penalty
-----------------------------------------------------------

.. code-block:: bash

   RNAfold --noPS --shape=tRNA.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-48.64)

This is ViennaRNA's default method and the one to start with. Each reactivity *r* is turned
into a pseudo-energy ΔG(r) = m · ln(r + 1) + b, with m = 1.8 and b = −0.6 kcal/mol by
default (Deigan et al. 2009), and that term is added for every nucleotide that takes part
in a stacked pair. A low reactivity gives a negative term, a bonus for pairing; a high
reactivity gives a positive term, a penalty. The folding algorithm is unchanged; only the
energies it sums are.

Two consequences follow. The energy printed, −48.64, is no longer a physical free energy:
it includes the pseudo-energies and cannot be compared with the −22.40 from the
unconstrained run. And the structure is the cloverleaf, as before; the data did not change
the answer. What they changed is how well supported it is, which the partition function
shows:

.. code-block:: bash

   RNAfold -p --noPS --shape=tRNA.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-48.64)
   (((((((..((((........)))).(((((.....,.))))).....(((((.......)))))))))))).... [-49.07]
   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... {-48.64 d=0.56}
    frequency of mfe structure in ensemble 0.49869; ensemble diversity 0.88

Without data: MFE frequency 0.06, diversity 23.4, a centroid with three pairs. With data:
MFE frequency 0.50, diversity 0.88, and the centroid is the cloverleaf itself. In the dot
plot, 20 of the 21 pairs of the cloverleaf now have probabilities of 0.98 or higher. The
exception is the terminal pair of the T stem, 49–65, at 0.39: a terminal pair next to the
multiloop takes part in only one stack and so receives the smallest share of the
pseudo-energy. The prediction did not move; the ensemble collapsed onto it.

The slope and intercept can be changed, for instance ``--shapeMethod="Dm1.9b-0.7"``, or one
of them alone (``"Dm1.9"``, ``"Db-0.7"``). A larger m makes the data weigh more against
the thermodynamic model. Unless you have calibrated your own experiment, keep the defaults;
they were fitted to normalised reactivities on a 0–2 scale, and data on a different scale
should be rescaled rather than compensated with m.

Method Z (Zarringhalam): penalise deviation from the data
---------------------------------------------------------

.. code-block:: bash

   RNAfold --noPS --shape=tRNA.shape --shapeMethod=Z < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-14.30)

Here the reactivities are first converted into a probability of being unpaired, and the
recursion is then penalised for every nucleotide whose predicted state deviates from that
probability. The strength of the penalty is set with ``--shapeMethod="Zb0.8"`` (β, default
0.89). The conversion from reactivity to probability is chosen with ``--shapeConversion``:
the default ``O`` fits a linear model to the logarithm of the reactivity; ``C0.25`` simply
calls everything above 0.25 unpaired; ``S`` skips the conversion if your file already
contains unpaired probabilities. For this profile Z gives the cloverleaf as well, with an
energy that again contains penalty terms and is not a free energy. With ``-p`` the MFE
structure has a frequency of 0.88 and the diversity is 0.27: on this clean profile Z
narrows the ensemble even further than D.

Method W (Washietl): a perturbation vector, computed first
----------------------------------------------------------

Method W is different in kind. It does not convert reactivities on the fly; it expects a
*perturbation vector*, a small energy correction for every nucleotide, chosen so that the
predicted unpaired probabilities agree with the data as well as possible while changing the
energy model as little as possible. That vector is computed by a separate program,
``RNApvmin``, which solves an optimisation problem:

.. code-block:: bash

   RNApvmin tRNA.shape < tRNA.fa > tRNA.pv
   RNAfold --noPS --shape=tRNA.pv --shapeMethod=W < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-24.44)

The perturbation vector for this profile holds corrections between −0.20 and +0.14
kcal/mol per nucleotide, most of them far smaller, and the result is the cloverleaf with an
energy close to the thermodynamic one; with ``-p`` the MFE frequency is 0.33 and the
diversity 8.9, so W intervenes least of the three. If you pass raw reactivities to
``--shapeMethod=W`` by mistake, RNAfold interprets them as energies and returns nonsense,
a mistake easy to make and easy to recognise, because the resulting structure bears no
relation to the data.

Which method to use? D is the default, the fastest and the most widely used; Z and W are
worth trying when you want to see how sensitive the result is to the way the data enter
the model. If the three agree, the conclusion is robust to that choice. If they disagree,
the data are not decisive for that region, which is itself worth knowing.

What the data change, and what they do not
------------------------------------------

Three small experiments make the behaviour concrete.

**Partial data.** Suppose only the anticodon loop, positions 32–38, was probed:

.. code-block:: bash

   awk '$1>=32 && $1<=38' tRNA.shape > partial.shape
   RNAfold --noPS --shape=partial.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... (-22.40)

Nothing changes, and the energy is the thermodynamic one, because the data agree with the
MFE structure at those positions and no other position received a term. Probing data only
act where they exist and only where they disagree with what the model would do anyway.

**Data that contradict the model.** Now set the reactivities of positions 1–7, the 5′ side
of the acceptor stem, to 1.2, as if those nucleotides had been found flexible:

.. code-block:: bash

   awk '{ if ($1<=7) printf "%d %s 1.20\n", $1, $2; else print }' tRNA.shape > contra.shape
   RNAfold -p --noPS --shape=contra.shape --shapeMethod=D < tRNA.fa

.. code-block:: text

   (((......((((........)))).(((((.......))))).....(((((.......)))))....))).... (-34.29)
   ((((((...((((........)))).(((((.......))))).....(((((.......))))).)))))).... {-34.07 d=2.18}
    frequency of mfe structure in ensemble 0.149346; ensemble diversity 3.04

The acceptor stem shrinks from seven pairs to three in the MFE structure. Positions 1–3
still pair despite their high reactivity, because the stacking energy of those three GC
pairs outweighs the penalty; and the centroid keeps six of the seven pairs, with the MFE
structure at 15 percent of the ensemble. This is what "soft constraint" means: the data
argue with the energy model, either side can win, and the ensemble shows how close the
contest was. A stronger slope, ``--shapeMethod="Dm2.6b-0.8"``, removes the acceptor stem
entirely. Hard constraints, which force positions to be unpaired (``RNAfold -C`` with a
constraint string), are a different tool for a different question.

**Consistent data.** As shown above, a profile consistent with the MFE structure leaves the
structure where it is and removes the alternatives from the ensemble. This is the common
case with good data on a well-folded RNA, and it is the useful one: probing turns "the MFE
structure, with 6 % support" into "the MFE structure, with half the ensemble behind it and
every pair but one above 0.98", which is the statement an experiment can be planned on.

Practical notes
---------------

- Normalise reactivities before use (the usual 2–8 % rule, or whatever your pipeline
  applies), and look at the distribution: a profile with almost all values near zero, or
  with a long tail above 3, is telling you about the experiment rather than the RNA.
- Reactivities measured in cells report on the RNA in its cellular context: bound
  proteins, ribosomes, ions. Folding such data with a model of the naked RNA is legitimate,
  but the result describes what a protein-free RNA with those constraints would do, not the
  cellular structure itself.
- Always run the partition function with the data. The MFE structure alone hides the main
  effect, which is on the probabilities.
- Report which method and parameters you used; the energies are not comparable across
  methods or with unconstrained folding.
- Keep the comparison to the unconstrained prediction. The regions where the data changed
  the structure are the regions where the thermodynamic model was uncertain; those are also
  the regions where the conclusion rests on the experiment, and where a second experiment
  is most informative.

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
