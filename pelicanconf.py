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
    '/services/workshops/': 'https://rnaforecast.com/',
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
    '/blog/2026/How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions/': '/blog/2015/SHAPE-directed-RNA-folding/',
    '/blog/2022/When-SHAPE-Data-Actually-Improves-RNA-Structure-Prediction/': '/blog/2015/SHAPE-directed-RNA-folding/',
    '/blog/2025/Why-Kinetic-Folding-Matters-in-RNA-Design/': '/blog/2025/kinpfn-rna-folding-kinetics/',
    '/blog/2026/When-to-trust-RNA-structure-prediction-for-experimental-decisions/': '/blog/2021/Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction/',
    '/blog/2026/When-sequence-conservation-is-not-enough-to-find-functional-RNA-structure/': '/blog/2021/Functional-RNA-Structures-in-the-3UTR-of-Mosquito-Borne-Flaviviruses/',
    '/blog/2025/What-AI-Can-and-Cannot-Do-for-RNA-Structure-and-RNA-Protein-Modeling/': '/blog/2021/Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction/',
    '/blog/2026/What-AI-Is-Genuinely-Useful-for-in-RNA-Biology/': '/blog/2021/Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction/',
    '/blog/2022/Cyclization-studies-of-Japanese-encephalitis-virus-non-coding-RNA-terminal-regions/': '/blog/2023/Investigating-RNA-RNA-interactions-through-computational-and-biophysical-analysis/',
}
