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
           'mtw_meta']

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
                'extra/llms.txt', 'extra/site.webmanifest', 'extra/redirects']
EXTRA_PATH_METADATA = {
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/robots.txt': {'path': 'robots.txt'},
                        'extra/favicon.ico': {'path': 'favicon.ico'},
                        'extra/llms.txt': {'path': 'llms.txt'},
                        'extra/site.webmanifest': {'path': 'site.webmanifest'},
                        # /services/ once existed; the URL stays alive as a no-index redirect to the home page
                        'extra/redirects/services.html': {'path': 'services/index.html'},
                        # merged tags: the old tag URLs redirect to the surviving tag
                        'extra/redirects/tag-virology.html': {'path': 'blog/tag/virology.html'},
                        'extra/redirects/tag-virology2.html': {'path': 'blog/tag/virology2.html'},
                        'extra/redirects/tag-virology3.html': {'path': 'blog/tag/virology3.html'},
                        'extra/redirects/tag-novel-viruses.html': {'path': 'blog/tag/novel-viruses.html'},
                        'extra/redirects/tag-agents.html': {'path': 'blog/tag/agents.html'},
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

