Deep learning for RNA secondary structure prediction
####################################################

:date: 2026-10-28
:tags: AI; ViennaRNA
:category: outreach
:section: essays
:slug: deep-learning-rna-secondary-structure-prediction
:title: AI for RNA structure prediction: what deep learning models learn
:summary: What neural networks trained on known RNA structures actually learn, why the usual benchmarks overstate their accuracy, what a test on synthetic data revealed about their outputs, and what has changed since 2022.
:description: What AI models for RNA secondary structure prediction learn from biased data, how to evaluate them on unseen families, and what has changed since 2022.
:social_image: {static}/static/og-ai-rna-structure-1200x630.png

.. role:: link-flat(link)
  :class: m-flat m-text

Whenever it comes to predicting RNA secondary structure from sequence, the question
nowadays is whether one should still use a thermodynamic folding program or rather one
of the neural networks that have been published for this task since about 2019. The
networks report higher accuracies than
:link-flat:`RNAfold <https://viennarna.readthedocs.io/en/latest/man/RNAfold.html>` or
:link-flat:`RNAstructure <https://rna.urmc.rochester.edu/RNAstructure.html>` on the standard
benchmarks, and the comparison looks settled at first glance. In this post I explain
what these predictors compute, why the benchmark numbers say less than they seem to,
what we found when we tested such networks on synthetic data with known properties
(:link-flat:`Flamm et al. 2022 <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`),
and what has happened in the field since then. The practical conclusion is given at the
end.

The classical approach and its limits
-------------------------------------

Energy directed folding, as implemented in RNAfold and related programs, computes the
structure of lowest free energy under the
:link-flat:`nearest-neighbor model <{filename}/glossary.rst#nearest-neighbor-model>`,
i.e. a table of free energies for small structural motifs (base pair stacks, hairpin,
interior and multi loops) that was measured in UV melting experiments. Under the
simplifying assumptions of that model, in particular the exclusion of
:link-flat:`pseudoknots <{filename}/glossary.rst#pseudoknot>` and base triples, the
optimal structure can be computed exactly by dynamic programming in cubic time, and the
same algorithms yield the :link-flat:`partition function <{filename}/glossary.rst#partition-function>`
and hence base pair probabilities for the whole ensemble.

The accuracy of this approach on known structures is limited. In the benchmark that
accompanied the 2004 Turner parameters, the
:link-flat:`MFE structure <{filename}/glossary.rst#mfe>` reproduced about two thirds
of the known base pairs on average, which is hardly more than with the 1999
parameters. It turned out that the limiting factor is the model itself
rather than the precision of the melting experiments, i.e. the simplifications that make
the dynamic programming possible are what costs accuracy, and this is the opening for
machine learning, since a model that does not have to be a sum of loop energies is free
to learn whatever regularities the known structures contain.

What the networks compute
-------------------------

The published deep learning predictors (SPOT-RNA, MXfold2, UFold and others) take a
sequence of length *n* and predict an *n* × *n* matrix in which the entry in row *i* and
column *j* indicates whether nucleotides *i* and *j* form a base pair. Convolutional
networks, residual blocks and in some cases recurrent layers operate on this matrix,
and a postprocessing step then turns the matrix of scores into a valid secondary
structure, e.g. by keeping the highest entry per row and removing crossing pairs.
Earlier attempts had tried to learn the energy parameters of the thermodynamic model from
data instead (CONTRAfold and the work of Andronescu and colleagues), whereas the network
approach drops the model altogether.

The training data for these methods come, with few exceptions, from the same small pool
of known structures; Szikszai et al. (2022) list the sets in use. The most used
collection, bpRNA, contains more than 100,000 sequences, which
sounds like a lot. However, 55 % of them are ribosomal RNAs from the Comparative RNA
Web site, and of the 43 % that come from Rfam, ribosomal RNAs and tRNAs again make up
more than 90 %. In practical terms the set is dominated by four RNA families, and the
length distribution has a sharp peak between 70 and 120 nucleotides, i.e. at the length
of tRNAs and 5S rRNAs.

Why the benchmark numbers overstate accuracy
--------------------------------------------

The standard way to evaluate a predictor is to split the available structures into a
training and a test set such that no two sequences are too similar, e.g. by requiring
less than 80 % sequence identity between the sets. For RNA this is not sufficient, as
structure is conserved far better than sequence, and two tRNAs with 60 % identity still
fold into the same cloverleaf. A network that has seen a few thousand tRNAs will predict
the cloverleaf for a tRNA it has never seen, and the benchmark counts this as a correct
de novo prediction. Rivas had already shown in 2013 that assembling test and training
sets from structurally distinct RNAs removes most of the advantage of learned over
measured energy parameters, and the same logic applies to networks.

The relevant question is therefore how a method performs on an RNA whose structure
class it has not seen, rather than how it performs within a family. Within-family
performance is of little practical interest anyway, since a sequence that belongs to a
known family should be assigned to that family with a covariance model (Infernal) and
mapped onto the consensus structure, which is in fact how most structures in bpRNA were
annotated in the first place. The honest benchmark hence puts whole families into either
the training or the test set, never both, e.g. the set of Rfam families added after
release 12.0 that the MXfold2 and UFold papers used to separate within-family from
cross-family performance.

The test on synthetic data
--------------------------

The difficulty with the biological data is that one cannot tell whether a network fails
because the training set is biased or because the architecture cannot represent the
problem. In the 2022 paper we therefore proposed to test the networks first on
synthetic data, i.e. on random sequences folded with RNAfold, which can be generated in
arbitrary amounts, are independent by construction and have a ground truth with known
statistical properties close to those of real structures (Fontana et al. 1993). A
network that cannot learn the simplified biophysical model from unlimited unbiased data
has little chance on the real thing.

In a deliberately simple first experiment we asked the networks to predict only whether
a nucleotide is paired or unpaired instead of base pairs, which is also the kind of
information one gets from chemical probing. Sliding window predictors, a
convolutional network and a bidirectional LSTM all reached an accuracy around 0.67 and a
Matthews correlation coefficient of at most 0.21 on 70-nucleotide sequences, and more
neurons or more data did not help. The networks had learned little beyond the fact that
an A is more often unpaired than a G. Pairedness is apparently not predictable without
the full structure, and the structure is too non-local for windows.

The second experiment used a re-implementation of the SPOT-RNA architecture to predict
base pair matrices. On sequences of uniform length (70 nt) the best model reached a
Matthews coefficient of 0.64, in line with what the SPOT-RNA authors report after initial
training. Several things then became visible that a benchmark on biological data cannot
show.

Networks trained on one length distribution performed worse on another, although all sets
were drawn from the same model and were perfectly independent. With sequences between 25
and 100 nucleotides, a network usually scored best on a test set with the length
distribution it had been trained on, and a network trained on mostly short sequences
performed poorly on longer ones. The bpRNA length peak at tRNA size is hence a bias in its
own right.

The number of predicted base pairs grew quadratically with sequence length. A secondary
structure of length *n* contains fewer than *n*/2 pairs, and the RNAfold ground truth
follows this line exactly, whereas all three network variants predicted a roughly constant
fraction of all *n* × *n* matrix entries before postprocessing (see Figure 3 of the
paper). The networks reproduced local properties very well, e.g. the relative frequencies
of GC, AU and GU pairs and the lengths of hairpin and interior loops, but not the global
constraint that follows from the one-dimensional nature of the chain. Multi loops, which
are rarer and less local, were predicted too long by nearly a factor of two.

The networks predicted pseudoknots and base triples although the training data contained
none. Of 2,000 predicted structures of length 100, 975 contained crossing pairs and 1,512
contained a nucleotide with more than one partner. The ability to predict pseudoknots is
often listed as an advantage of networks over dynamic programming. If a network predicts
them for a ground truth that has none, it is not clear what the pseudoknots mean when the
ground truth is unknown.

Finally, the effect of the dataset bias could be measured directly. We built a training
set with the structure bias of bpRNA by inverse folding the bpRNA structures (those
between 25 and 120 nucleotides, with pseudoknots removed) into new random sequences with
RNAinverse, i.e. the same structures with completely different sequences. The network
reached a Matthews coefficient of 0.86 on a test set with the same structure bias, and
0.52 on a test set of dinucleotide-shuffled sequences with the same composition but the
structural diversity of random RNA. In other words, novel sequences were no obstacle for
the network, whereas novel structures were. A network trained on bpRNA generalizes well to
sequences it has never seen as long as their structure is in the training set, and this is
precisely what the usual benchmark rewards.

What has changed since 2022
---------------------------

The evaluation problem has since been confirmed independently. Szikszai and colleagues
(Bioinformatics 38, 3892, 2022) proposed inter-family cross-validation and found that
the deep learning models they could retrain did not generalize across families, while
for the others the published splits had not accounted for homology. Justyna, Antczak and
Szachniuk (Briefings in Bioinformatics 24, bbad153, 2023) benchmarked six deep learning,
three shallow learning and six classical methods on experimentally determined structures
and on new Rfam families. The deep learning methods won when training and test data
followed the same distribution, and on new families their advantage disappeared, with
performance equal to or below that of the classical methods. Family-level splits have
since become the expected standard in the field, which is the main thing the caveats
papers achieved.

The data situation has started to change with the Ribonanza project (He et al., bioRxiv
2024), which collected chemical mapping data for about two million designed and natural RNA
sequences through Eterna and a Kaggle competition and distilled the best competition
entries into a single model, RibonanzaNet. Reactivity profiles are a different kind of
training signal in that they are measured, they exist for sequences that belong to no
family, and a model trained on them predicts an experimental observable rather than an
annotated structure. Whether such models capture folding rules or the design space of
the measured library is again a question of the test set, nevertheless the volume and
independence of the data are of a different order than bpRNA.

For three-dimensional structure, AlphaFold 3 (Abramson et al., Nature 630, 493, 2024)
extended the protein architecture to nucleic acids. An independent benchmark by Bernard
and colleagues (Acta Crystallographica D 81, 49, 2025) found it ahead of most dedicated
RNA methods and of the other deep learning approaches, and still behind the best
human-guided submissions on the CASP RNA targets. The CASP16 assessment of nucleic acid
prediction (Kretsch et al., 2026) draws a similar picture. Predicted canonical base
pairs, i.e. the secondary structure, were accurate and better than the common folding
algorithms, accuracy dropped for crossing, isolated and non-canonical pairs, no blind
prediction of a previously unseen natural RNA reached a TM-score of 0.8, and the main
determinant of 3D accuracy was whether a related experimental structure existed. The
pattern from 2022 is visible here as well, i.e. what is local and well represented in
the data is learned, whereas what is global, rare or novel is not.

Consequences for practice
-------------------------

Several things follow for anyone who has to decide what to run on a new sequence.

An RNA that belongs to a known family should be assigned to it with Infernal and folded
onto the consensus structure, as there is no better predictor than a curated alignment.
Prediction from sequence is for the remaining cases, and these are by definition the
cases on which networks trained on bpRNA have not been tested in a meaningful way.

For such sequences, the thermodynamic ensemble is still the reference point. Its errors
are understood, it does not depend on what happened to be in a database, and it produces
base pair probabilities that state which parts of the prediction are supported and which
are not (how to read them is the subject of the
:link-flat:`RNAfold tutorial <{filename}/blog/2026-10-28-rnafold-in-practice.rst>`).
Where experimental data exist, probing reactivities can be folded into the model as
:link-flat:`soft constraints <{filename}/glossary.rst#soft-constraints>` (see
:link-flat:`Lorenz et al. 2016 <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`
and the :link-flat:`SHAPE tutorial <{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst>`),
which addresses the limits of the energy model with a measurement rather than with a
prior learned from other RNAs.

When a network is used, its output should be checked for structural validity before
anything else, i.e. whether the number of pairs is plausible for the length, whether
nucleotides have more than one partner, and whether predicted pseudoknots survive a
sanity check against the thermodynamics of the two helices involved. These are cheap
checks and they catch exactly the artifacts that the synthetic data test revealed.

When a paper about a network is read, the first thing to look for is the split, since a
test set that shares families with the training set measures recognition of known
structures, which is a legitimate task but a different one. Accuracy on families withheld
entirely from training, or on structures determined after the training set was
assembled, is the number that matters, and it is usually much lower. None of this is an
argument against learning from data. The 2022 paper argued for testing architectures on
synthetic data first and for benchmarks that separate memorization from generalization,
and the developments since then point in the same direction.

Further reading
---------------

- Flamm C, Wielach J, Wolfinger MT, Badelt S, Lorenz R, Hofacker IL. Caveats to deep
  learning approaches to RNA secondary structure prediction. *Front Bioinform* 2:835422
  (2022). doi:10.3389/fbinf.2022.835422. On this site:
  :link-flat:`the paper page <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`.
  Data and code at :link-flat:`github.com/ViennaRNA/rnadeep <https://github.com/ViennaRNA/rnadeep>`.
- Szikszai M, Wise M, Datta A, Ward M, Mathews DH. Deep learning models for RNA
  secondary structure prediction (probably) do not generalize across families.
  *Bioinformatics* 38:3892–3899 (2022). doi:10.1093/bioinformatics/btac415.
- Justyna M, Antczak M, Szachniuk M. Machine learning for RNA 2D structure prediction
  benchmarked on experimental data. *Brief Bioinform* 24:bbad153 (2023).
  doi:10.1093/bib/bbad153.
- Rivas E. The four ingredients of single-sequence RNA secondary structure prediction.
  A unifying perspective. *RNA Biol* 10:1185–1196 (2013). doi:10.4161/rna.24971.
- Fontana W, Konings DAM, Stadler PF, Schuster P. Statistics of RNA secondary structures.
  *Biopolymers* 33:1389–1404 (1993). doi:10.1002/bip.360330909.
- He S, et al. Ribonanza: deep learning of RNA structure through dual crowdsourcing.
  *bioRxiv* (2024). doi:10.1101/2024.02.24.581671.
- Abramson J, et al. Accurate structure prediction of biomolecular interactions with
  AlphaFold 3. *Nature* 630:493–500 (2024). doi:10.1038/s41586-024-07487-w.
- Bernard C, Postic G, Ghannay S, Tahi F. Has AlphaFold3 achieved success for RNA?
  *Acta Crystallogr D* 81:49–62 (2025). doi:10.1107/S2059798325000592.
- Kretsch RC, Hummer AM, He S, Yuan R, Zhang J, Karagianes T, Cong Q, Kryshtafovych A,
  Das R. Assessment of nucleic acid structure prediction in CASP16. *Proteins* 94:192–217
  (2026). doi:10.1002/prot.70072.
- Lorenz R, Wolfinger MT, Tanzer A, Hofacker IL. Predicting RNA secondary structures
  from sequence and probing data. *Methods* 103:86–98 (2016).
  doi:10.1016/j.ymeth.2016.04.004.
