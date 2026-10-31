#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'Michael T. Wolfinger'
SITENAME = "Michael T. Wolfinger"
SITEURL = ''
OUTPUT_PATH = 'output'

PATH = 'content'
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['']
PAGE_EXCLUDES = ['extra']   # static extras (robots, redirects, ...) are not pages

# Explicit so local and CI builds render dates identically regardless of locale.
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
TIMEZONE = 'Europe/Vienna'
DEFAULT_DATE = None

DEFAULT_LANG = 'en'

THEME = 'pelican-theme'
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static']

DIRECT_TEMPLATES = ['index']
# Plain-text companion to llms.txt, rendered from the article and page metadata.
TEMPLATE_PAGES = {'llms-full.txt': 'llms-full.txt'}

FORMATTED_FIELDS = ['summary', 'landing', 'footer', 'description']

# The web fonts are self-hosted (static/fonts/, declared at the top of m-mtw.css), so the
# stylesheet is the only CSS request and nothing is fetched from Google.
M_CSS_FILES = [
    'static/m-mtw.css',
]

M_THEME_COLOR = '#f1f0ec'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['m.htmlsanity',
           'm.components',
           'm.link',
           'm.sitemap',
           'm.images',
           'mtw_meta',
           'mtw_doi',
           'mtw_redirects']

# Category listings are disallowed in robots.txt and the publications/papers/ stubs are
# canonicalised to their blog posts, so neither belongs in the sitemap. (Redirect stubs
# under extra/redirects/ are static files and never reach the sitemap generator.)
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "weekly",
        "pages": "monthly"
    },
    "exclude": ["blog/archive/", "blog/author/", "blog/category/",
                "authors", "index", "publications/papers/", "404", "llms"]
}

# Links carry the trailing slash: that is the canonical form of every page URL, and the
# slash-less form costs a redirect on GitHub Pages.
M_LINKS_NAVBAR1 = [
                    ('About', '/about/', 'about', []),
                    ('Research', '/research/', 'research', [
                        ('Team', '/team/', 'team'),
                        ('Collaborations', '/collaborations/', 'collaborations'),
                    ]),
                    ('Publications', '/publications/', 'publications', [
                        ('Papers', '/publications/', 'papers'),
                        ('Presentations', '/publications/presentations/', 'publications/presentations'),
                        ('Posters', '/publications/posters/', 'publications/posters'),
                        ]),
                    ('Teaching', '/teaching/', 'teaching', []),
                    ('Guides', '/rna-structure-prediction/', 'rna-structure-prediction', [
                        ('RNA structure prediction', '/rna-structure-prediction/', 'rna-structure-prediction'),
                        ('Flavivirus RNA structures', '/flavivirus-rna-structures/', 'flavivirus-rna-structures'),
                        ('RNA folding kinetics', '/rna-folding-kinetics/', 'rna-folding-kinetics'),
                    ]),
                    ('Contact', '/contact/', 'contact', []),
                    ('Writing', '/blog/', '[blog]',[])]

# Footer: four link columns as in the mockups. The first entry of each list is the
# column heading (linked when it has a URL).
M_LINKS_FOOTER1 = [('Home', '/'),
                    ('About', '/about/'),
                    ('Research', '/research/'),
                    ('Publications', '/publications/'),
                    ('Teaching', '/teaching/'),
                    ('People & Supervision', '/team/'),
                    ('Writing', '/blog/'),
                    ]

M_LINKS_FOOTER2 = [('More', ''),
                    ('RNA structure guides', '/rna-structure-prediction/'),
                   ('Flavivirus RNA structures', '/flavivirus-rna-structures/'),
                   ('RNA folding kinetics', '/rna-folding-kinetics/'),
                    ('Glossary', '/glossary/'),
                    ('RNA Forecast', 'https://rnaforecast.com'),
                    ('Contact', '/contact/'),
                    ('Impressum', '/legal/'),
                    ('Datenschutz', '/datenschutz/'),
                    ('Cookie settings', '#cookie-settings'),
                    ]

M_LINKS_FOOTER3 = [('My Profiles', ''),
                    ('Google Scholar', 'https://scholar.google.at/citations?user=w0PHGnEAAAAJ&hl=en'),
                    ('ResearchGate', 'https://www.researchgate.net/profile/Michael-Wolfinger'),
                    ('Scopus', 'https://www.scopus.com/authid/detail.uri?authorId=6508361997'),
                    ('Loop', 'https://loop.frontiersin.org/people/485709/overview'),
                    ]

M_LINKS_FOOTER4 = [('Social', ''),
                    ('LinkedIn', 'https://www.linkedin.com/in/michaelwolfinger/'),
                    ('Bluesky', 'https://bsky.app/profile/mtwolfinger.bsky.social'),
                    ('GitHub', 'https://github.com/mtw'),
                    ('ORCID', 'https://orcid.org/0000-0003-0925-5205'),
                    ]

M_FINE_PRINT = "© %d Michael T. Wolfinger · Vienna, Austria · michael.wolfinger@rnaforecast.com" % datetime.date.today().year

STATIC_PATHS = ['static', 'extra/CNAME', 'extra/robots.txt', 'extra/favicon.ico',
                'extra/llms.txt', 'extra/site.webmanifest', 'extra/legacy']
EXTRA_PATH_METADATA = {
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/robots.txt': {'path': 'robots.txt'},
                        'extra/favicon.ico': {'path': 'favicon.ico'},
                        'extra/llms.txt': {'path': 'llms.txt'},
                        'extra/site.webmanifest': {'path': 'site.webmanifest'},
                        # two talk PDFs were renamed after their real dates; the old names stay downloadable
                        'extra/legacy/2020-10-15-Kent.pdf': {'path': 'files/presentations/2020-10-15-Kent.pdf'},
                        'extra/legacy/2013-03-05-CIBIV.pdf': {'path': 'files/presentations/2013-03-05-CIBIV.pdf'},
                        }

RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Display names for the blog categories (the category slug stays as it is).
M_CATEGORY_LABELS = {'howto': 'How-to', 'outreach': 'Outreach', 'publications': 'Publications'}

# The three guide tiles on the landing page, by article slug and in this order; the
# "Latest writing" list below them skips these posts.
HOME_GUIDES = ['rnafold-in-practice',
               'How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions',
               'deep-learning-rna-secondary-structure-prediction']

M_BLOG_NAME = "Notes & Writing"   # matches the nav entry "Writing" and the blog H1
M_BLOG_URL = 'https://michaelwolfinger.com/blog/'
M_BLOG_DESCRIPTION = "Notes on computational RNA biology by Michael T. Wolfinger: RNA structure, folding dynamics, functional RNA design, and structured viral RNAs."

M_SOCIAL_TWITTER_SITE = '@mtwolfinger'
M_SOCIAL_TWITTER_SITE_ID = 15105886
# Link-preview card (Open Graph / Twitter), 1200x630; source in tools/og-cards-source.html.
M_SOCIAL_IMAGE = '/static/og-wide-1200x630.png'
M_SOCIAL_IMAGE_WIDTH = 1200
M_SOCIAL_IMAGE_HEIGHT = 630
M_SOCIAL_IMAGE_ALT = 'RNA Structure, Function & Design - Michael T. Wolfinger, michaelwolfinger.com'
M_SOCIAL_CARD = 'summary_large_image'
# Portrait used as the Person image in structured data.
M_PERSON_IMAGE = '/static/mtw.jpg'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = ''
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
INDEX_URL = 'blog/'   # read by the sitemap plugin; without it the blog index is written as '/'
INDEX_SAVE_AS = 'blog/index.html'

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'

DEFAULT_PAGINATION = 5


# URLs that once existed and still appear in search results or bookmarks. plugins/mtw_redirects.py
# writes a no-index page with a meta refresh at each old path. Keys are site-relative old
# paths; values are site-relative or absolute targets.
REDIRECTS = {
    # former commercial pages: the offers live on rnaforecast.com
    '/services/': 'https://rnaforecast.com/',
    '/services/workshops/': 'https://rnaforecast.com/training/',
    '/consulting/': 'https://rnaforecast.com/',
    # merged tags
    '/blog/tag/virology.html': '/blog/tag/virus-bioinformatics.html',
    '/blog/tag/virology2.html': '/blog/tag/virus-bioinformatics.html',
    '/blog/tag/virology3.html': '/blog/tag/virus-bioinformatics.html',
    '/blog/tag/novel-viruses.html': '/blog/tag/virus-bioinformatics.html',
    '/blog/tag/agents.html': '/blog/tag/ai.html',
    # tag pages from before the relaunch
    '/blog/tag/rna-kinetics.html': '/blog/tag/rna-folding-kinetics.html',
    '/blog/tag/co-transcriptional-rna-folding2.html': '/blog/tag/co-transcriptional-rna-folding.html',
    '/blog/tag/rna-structure-prediction2.html': '/blog/tag/rna-structure-prediction.html',
    '/blog/tag/viruses/index2.html': '/blog/tag/virus-bioinformatics.html',
    # post URLs from before the relaunch (date-prefixed slugs under blog/<year>/blog/)
    '/blog/2024/blog/2024-02-12-A-framework-for-automated-scalable-designation-of-viral-pathogen-lineages-from-genomic-data/': '/blog/2024/automated-viral-lineage-designation/',
    '/blog/2023/blog/2023-06-09-A-Structural-Refinement-Technique-for-Protein-RNA-Complexes-Using-Combination-of-AI-based-Modeling-and-Flexible-Docking-A-Study-of-Musashi-1-Protein/': '/blog/2023/rna-protein-complex-refinement-musashi-1/',
    '/blog/2024/blog/2024-05-29-Xingyang-flavivirus-from-Haemaphysalis-flava-ticks-defines-a-basal-likely-tick-only-Orthoflavivirus-clade/': '/blog/2024/xinyang-flavivirus-tick-only-orthoflavivirus-clade/',
    '/blog/2024/blog/2024-10-15-Pan-flavivirus-analysis-reveals-sfRNA-independent-3-UTR-biased-siRNA-production-from-an-insect-specific-flavivirus/': '/blog/2024/pan-flavivirus-sirna-production-in-insect-specific-flavivirus/',
    '/blog/2017/blog/2017-01-31-NMR-Structural-Profiling-of-Transcriptional-Intermediates-Reveals-Riboswitch-Regulation-by-Metastable-RNA-Conformations/': '/blog/2017/co-transcriptional-riboswitch-metastable-states/',
    '/blog/2025/blog/2025-07-29-Functional-RNAs-in-Virology/': '/blog/2025/functional-rnas-in-virology/',
    '/blog/2025/blog/2025-07-18-Exploring-RNA-Biology-with-Deep-Learning/': '/blog/2025/exploring-rna-biology-with-deep-learning/',
    '/blog/2020/blog/2020-12-10-Genomic-Epidemiology-of-Superspreading-Events-in-Austria-Reveals-Mutational-Dynamics-and-Transmission-Properties-of-SARS-CoV-2/': '/blog/2020/genomic-epidemiology-sars-cov-2-austria/',
    # legacy paper stubs that no longer exist
    '/publications/papers/An_African_Tick_Flavivirus_Forming_an_Independent_Clade_Exhibits_Unique_Exoribonuclease-Resistant_RNA_Structures_in_the_Genomic_three_prime-Untranslated_Region/': '/blog/2021/Mpulungu_Virus_is_a_novel_tick_flavivirus_from_Africa/',
    '/publications/papers/Musashi_Binding_Elements_in_Zika_and_Related_Flavivirus_3UTRs_A_Comparative_Study_in_Silico/': '/blog/2019/Musashi-Binding-Elements-in-Zika-and-Related-Flavivirus-3UTRs-A-Comparative-Study-in-Silico/',
    '/publications/papers/Functional_RNA_Structures_in_the_3UTR_of_Tick-Borne_Insect-Specific_and_No_Known_Vector_Flaviviruses/': '/blog/2019/Functional_RNA_Structures_in_the_three_prime_UTR_of_Flaviviruses/',
    '/publications/papers/Genomic_Epidemiology_of_Superspreading_Events_in_Austria_Reveals_Mutational_Dynamics_and_Transmission_Properties_of_SARS-CoV-2/': '/blog/2020/genomic-epidemiology-sars-cov-2-austria/',
    # drafts and hidden posts that were removed; the nearest published post on the topic
    '/blog/2022/When-SHAPE-Data-Actually-Improves-RNA-Structure-Prediction/': '/blog/2015/SHAPE-directed-RNA-folding/',
    '/blog/2025/Why-Kinetic-Folding-Matters-in-RNA-Design/': '/blog/2025/kinpfn-rna-folding-kinetics/',
    '/blog/2026/When-to-trust-RNA-structure-prediction-for-experimental-decisions/': '/blog/2026/rnafold-in-practice/',
    '/blog/2026/When-sequence-conservation-is-not-enough-to-find-functional-RNA-structure/': '/blog/2021/Functional-RNA-Structures-in-the-3UTR-of-Mosquito-Borne-Flaviviruses/',
    # the two AI essays were superseded by the 2026 explainer, which answers the same question
    '/blog/2025/What-AI-Can-and-Cannot-Do-for-RNA-Structure-and-RNA-Protein-Modeling/': '/blog/2026/deep-learning-rna-secondary-structure-prediction/',
    '/blog/2026/What-AI-Is-Genuinely-Useful-for-in-RNA-Biology/': '/blog/2026/deep-learning-rna-secondary-structure-prediction/',
    '/blog/2022/Cyclization-studies-of-Japanese-encephalitis-virus-non-coding-RNA-terminal-regions/': '/blog/2023/Investigating-RNA-RNA-interactions-through-computational-and-biophysical-analysis/',
}


# Topic introductions for tag pages. A tag listed here renders as a topic page: its own
# title, description and an introduction above the post list (page 1 only); every other
# tag keeps the plain "Posts tagged …" listing. Keys are the tag slugs, links are
# root-relative and prefixed with SITEURL in tag.html.
M_TAG_INTROS = {
    'viennarna': {
        'heading': 'ViennaRNA',
        'title': 'ViennaRNA: papers, tutorials and notes',
        'description': 'Papers, tutorials and notes on the ViennaRNA Package: RNAfold output, SHAPE data as soft constraints, co-transcriptional folding.',
        'intro': '''<p>The ViennaRNA Package implements the thermodynamic model of RNA secondary structure: minimum free energy folding, the partition function with base pair probabilities, suboptimal structures, consensus structures and folding kinetics, as command-line programs and as a C and Python library. I have been working with and on the package since its early days, e.g. on the integration of chemical probing data and on co-transcriptional folding, and it is the tool behind most of the work on this site.</p>
<p>The posts collected here are the papers that extended the package (soft constraints for SHAPE reactivities, co-transcriptional folding with ligands), the two tutorials on reading RNAfold output and on folding with probing data, and the explainer on deep learning predictors. The page <a href="/rna-structure-prediction/">RNA structure prediction with ViennaRNA</a> orders them for a reader who starts from a question; the <a href="/glossary/#viennarna">glossary</a> defines the terms.</p>''',
    },
    'xrrna': {
        'heading': 'Exoribonuclease-resistant RNAs',
        'title': 'Exoribonuclease-resistant RNAs (xrRNAs)',
        'description': 'Exoribonuclease-resistant RNAs in flavivirus 3′UTRs: how xrRNAs stall Xrn1, where they occur across flavivirus lineages, and how they can be designed.',
        'intro': '''<p>Exoribonuclease-resistant RNAs (xrRNAs) are structured elements in the 3&prime; untranslated region of flavivirus genomes that stall the host 5&prime;&ndash;3&prime; exoribonuclease Xrn1. The viral RNA downstream of the stall survives as subgenomic flaviviral RNA (sfRNA), which interferes with the antiviral response of the host. The resistance is mechanical: a ring-like fold with a pseudoknot closes over the 5&prime; end of the element and holds against the pulling enzyme.</p>
<p>The posts here cover comparative studies of xrRNAs across mosquito-borne, tick-borne and insect-specific flaviviruses, the discovery of new variants in viruses from Zambia and in a novel African tick flavivirus, their conservation within tick-borne encephalitis virus, and recent work on designing mechanically active RNAs from scratch. The terms are defined in the glossary under <a href="/glossary/#xrrna">xrRNA</a> and <a href="/glossary/#sfrna">sfRNA</a>.</p>''',
    },
    'flavivirus': {
        'heading': 'Flavivirus RNA structures',
        'title': 'Flavivirus RNA structures',
        'description': 'Conserved RNA structures in flavivirus genomes: 3′UTR elements across virus lineages, the Zika G-quadruplex, cyclization, molecular epidemiology.',
        'intro': '''<p>Flaviviruses (dengue, Zika, West Nile, tick-borne encephalitis virus and many viruses without a known vector or vertebrate host) carry a positive-strand RNA genome of about 11 kb whose untranslated regions are densely structured. The 3&prime;UTR in particular is a succession of conserved elements: exoribonuclease-resistant RNAs, dumbbells, stem-loops and the cyclization sequences that pair with the 5&prime; end of the genome.</p>
<p>Most of the work collected here is comparative: structures predicted and checked across hundreds of genomes, which shows what is conserved in a lineage and what is specific to a host or a vector. Other posts look at single elements in detail (the G-quadruplex at the Zika 3&prime; end, RNA&ndash;RNA interactions in Japanese encephalitis virus) or connect structure conservation with molecular epidemiology. See <a href="/glossary/#flavivirus">flavivirus</a> and <a href="/glossary/#utr3">3&prime; UTR</a> in the glossary.</p>''',
    },
    'rna-folding-kinetics': {
        'heading': 'RNA folding kinetics',
        'title': 'RNA folding kinetics',
        'description': 'RNA folding kinetics: from barrier trees and macrostate dynamics to co-transcriptional folding and learned folding time distributions, 2004 to 2025.',
        'intro': '''<p>An RNA molecule does not simply adopt its minimum free energy structure. It folds along paths through a landscape of alternative structures, can be trapped in metastable states, and in the cell the chain folds while it is being transcribed. Folding kinetics asks how fast and by which route a structure is reached, and for riboswitches and designed switches that answer matters more than the final structure.</p>
<p>The posts here follow one line of work: coarse-grained dynamics on barrier trees (Barriers and Treekin), the extension to landscapes that change over time (BarMap), co-transcriptional folding with and without ligands, and recent approaches that learn folding time distributions directly (KinPFN). The glossary explains <a href="/glossary/#folding-kinetics">folding kinetics</a>, <a href="/glossary/#macrostate">macrostates</a> and <a href="/glossary/#metastable-state">metastable states</a>.</p>''',
    },
    'energy-landscapes': {
        'heading': 'Energy landscapes',
        'title': 'RNA energy landscapes and barrier trees',
        'description': 'Energy landscapes of RNA and lattice proteins: local minima, saddle points, barrier trees, their efficient computation.',
        'intro': '''<p>The energy landscape of an RNA sequence is the set of all its secondary structures with their free energies, connected by elementary moves, i.e. opening or closing one base pair. Its local minima are the structures a molecule can rest in, the saddle points between them set the barriers, and the barrier tree summarises this topology in one diagram. Coarse-graining the landscape into basins turns an astronomically large structure space into a Markov process that can be solved.</p>
<p>The posts begin with the 2002 barrier-tree paper on degenerate landscapes and the lattice protein models that served as test systems, continue with methods for exploring the low-energy part of a landscape efficiently, and end with applications to co-transcriptional folding and RNA design. See <a href="/glossary/#energy-landscape">energy landscape</a>, <a href="/glossary/#barrier-tree">barrier tree</a> and <a href="/glossary/#saddle-point">saddle point</a>.</p>''',
    },
    'rna-design': {
        'heading': 'RNA design',
        'title': 'RNA design: switches and mechanically active RNAs',
        'description': 'Designing RNA sequences for a function: ligand-triggered switches with kinetic criteria, probing-data informed design, and mechanically active RNAs.',
        'intro': '''<p>RNA design is the inverse of structure prediction: given a target structure, or a set of structures a molecule should switch between, find a sequence that folds accordingly. The thermodynamic model makes this a well-posed computational problem, and the same model then says why a candidate fails, e.g. because the switching path is slow or passes through an off-target intermediate.</p>
<p>The posts here cover the design of ligand-triggered riboswitches with explicit kinetic criteria, the use of probing data in design decisions, an essay on mRNA vaccine design, and the rational design of mechanically active RNAs that resist an exoribonuclease, a direction that grew out of the flavivirus xrRNA work. The glossary defines <a href="/glossary/#ensemble-defect">ensemble defect</a> and <a href="/glossary/#xrrna">xrRNA</a>.</p>''',
    },
    'rna-protein-interaction': {
        'heading': 'RNA–protein interaction',
        'title': 'RNA–protein recognition',
        'description': 'How proteins recognise RNA: Musashi-1 binding to flavivirus 3′UTRs, molecular dynamics and AI-assisted refinement of RNA-protein complexes.',
        'intro': '''<p>Most functional RNA acts together with proteins, and the specificity of that recognition is decided by structure on both sides: the RNA has to present its binding motif in an accessible conformation, and the RNA-binding domains of the protein have to fit it. The computational work here combines sequence and structure analysis of the RNA with molecular dynamics and docking of the complex.</p>
<p>The posts follow the RNA-binding protein Musashi-1 from a comparative study of its binding elements in Zika and related flavivirus 3&prime;UTRs, through molecular dynamics of its two RNA-binding domains, to a refinement protocol for RNA&ndash;protein complexes that combines AI-based modelling with flexible docking. Two posts on archaeal Sm-like proteins and the translation factor aIF5A complete the set. The glossary entry <a href="/glossary/#musashi">Musashi</a> gives the background.</p>''',
    },
    'co-transcriptional-rna-folding': {
        'heading': 'Co-transcriptional RNA folding',
        'title': 'Co-transcriptional RNA folding',
        'description': 'Co-transcriptional RNA folding: how a growing chain folds during transcription, metastable intermediates in riboswitches, and BarMap.',
        'intro': '''<p>In the cell an RNA molecule starts to fold while it is still being made. The polymerase adds a few tens of nucleotides per second, and the 5&prime; part of the chain has long found a structure before the 3&prime; part exists. Structures formed early can persist as metastable states, so the final structure depends on the transcription history and not only on the sequence.</p>
<p>The posts here describe the formalism for folding on a landscape that changes with every added nucleotide (BarMap), its application to riboswitches whose function depends on such intermediates, the inclusion of ligand binding into the kinetics, and the design of switches that take the transcriptional path into account. See <a href="/glossary/#cotranscriptional-folding">co-transcriptional folding</a> and <a href="/glossary/#barmap">BarMap</a> in the glossary.</p>''',
    },
    'shape': {
        'heading': 'SHAPE and chemical probing',
        'title': 'SHAPE and chemical probing data',
        'description': 'SHAPE and chemical probing data in RNA structure prediction: reactivities as soft constraints in ViennaRNA, the methods, and a tutorial with examples.',
        'intro': '''<p>Chemical probing experiments (SHAPE, DMS and related methods) report, per nucleotide, how reactive a position is to a reagent, and thus how likely it is to be unpaired. The data do not give a structure. They become useful when they enter a structure prediction as soft constraints, i.e. as pseudo-energies that shift the thermodynamic model toward structures compatible with the measurement.</p>
<p>The posts here are the two methods papers that brought this into ViennaRNA (the comparison of SHAPE-to-pseudo-energy conversions, and the perturbation-vector approach), an application to the BVDV IRES, and the tutorial that walks through folding with reactivities in RNAfold, including what to do with partial data. The glossary covers <a href="/glossary/#shape">SHAPE</a>, <a href="/glossary/#reactivity">reactivity</a> and <a href="/glossary/#soft-constraints">soft constraints</a>.</p>''',
    },
}
