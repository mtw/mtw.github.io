What AI can and cannot do for RNA structure and RNA-protein modeling
####################################################################

:date: 2025-02-01
:modified: 2026-04-30
:tags: AI; RNA structure prediction; RNA-Protein interaction; 3D
:category: outreach
:slug: What-AI-Can-and-Cannot-Do-for-RNA-Structure-and-RNA-Protein-Modeling
:author: mtw
:summary: AI has become useful in RNA structure and RNA-protein modeling, but its real value depends on where the biological uncertainty lies and how the models are checked against physics and experiment.
:title: What AI can and cannot do for RNA structure and RNA-protein modeling
:description: A researcher’s view on where AI helps in RNA structure prediction and RNA-protein complex modeling, and where it still needs experimental and physical grounding.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/figures/RNP_complex_network1.webp
          :alt: RNA protein complex embedded in a network
          :figclass: m-figure m-flat


AI has become impossible to ignore in RNA biology, and with good reason. Machine learning now contributes to sequence annotation, structure scoring, kinetics approximation, and the generation of candidate models for RNA-protein complexes. Trouble starts when “AI for RNA” is treated as a single activity, because those tasks differ sharply in what they can actually tell us.

For a broader view across RNA biology, beyond structure and protein-RNA modeling specifically, see :link-flat:`What AI is genuinely useful for in RNA biology <{filename}/blog/2026-03-22-What-AI-Is-Genuinely-Useful-for-in-RNA-Biology.rst>`. That piece looks more explicitly at candidate ranking, kinetics approximation, and large-scale genomic organization in addition to structural modeling.

The first distinction that matters is between prediction and interpretation. A model may produce a plausible structure, a useful ranking, or a good benchmark score without actually resolving the biological uncertainty that motivated the analysis. :link-flat:`Caveats to deep learning approaches to RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>` makes that point very clearly. Good performance on familiar datasets does not guarantee generalization to new sequence families, new experimental conditions, or regulatory RNAs that occupy multiple states.

The second distinction is between static coordinates and mechanistic explanation. In RNA-protein systems, AI-derived models can be extremely useful as starting points. They can place domains sensibly, suggest contact regions, and reduce the search space. But they often do not settle the central question, which is whether the proposed geometry really explains specificity, accessibility, competition, or function. That is why :link-flat:`A structural refinement technique for protein-RNA complexes using a combination of AI-based modeling and flexible docking <{filename}/blog/2023-06-09-A-Structural-Refinement-Technique-for-Protein-RNA-Complexes-Using-Combination-of-AI-based-Modeling-and-Flexible-Docking-A-Study-of-Musashi-1-Protein.rst>` matters. Refinement, docking, and consistency checks still change the conclusion.

The Musashi line of work makes this especially clear. :link-flat:`Theoretical studies on RNA recognition by Musashi1 RNA-binding protein <{filename}/blog/2022-07-26-Theoretical-studies-on-RNA-recognition-by-Musashi1-RNA-binding-protein.rst>` asks which motifs bind better and why. :link-flat:`From Structure to Function: Computational Insights into Musashi-RNA Complexes <{filename}/blog/2025-01-01-From-Structure-to-Function-Computational-Insights-into-Musashi-RNA-Complexes.rst>` then steps back and asks how those structural observations connect to a broader functional picture. AI helps in that workflow, but it does not replace the need for energetic reasoning, dynamics, or biological interpretation.

Kinetics offers a similar lesson. :link-flat:`KinPFN: Bayesian Approximation of RNA Folding Kinetics <{filename}/blog/2025-01-01-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst>` is interesting precisely because it does not pretend to solve folding physics from scratch. It uses AI as an approximation layer on top of a physically meaningful problem. In RNA work, that is often the most convincing role for machine learning. It speeds up an existing analysis framework or helps prioritize candidates without asking the reader to trust a black box on faith.

So where does AI help most right now? It is most useful when the task is to rank candidates, propose starting models, or shorten an otherwise expensive round of inference. It is also easier to trust when there is still a clear route back to physics, experiment, or comparative evidence. Confidence scores on their own are much less persuasive.

For researchers and teams, the practical issue is usually not whether AI should be used at all. The harder question is where to trust it, where to test it more aggressively, and where to combine it with other forms of evidence. That judgment becomes especially difficult when the output looks polished and the project is under time pressure. In that situation, what helps is rarely more enthusiasm. What helps is a careful review of the modeling assumptions, the likely failure modes, and the decision that actually has to be made. My :link-flat:`services page <{filename}/services.rst>` describes the formats I use for that kind of focused review and advisory support.
