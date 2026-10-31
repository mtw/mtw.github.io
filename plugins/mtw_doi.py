"""Turn plain DOI mentions into links.

The reference lists on this site write DOIs as text, ``doi:10.1093/bioinformatics/btac415``.
This plugin links every such mention to https://doi.org/<doi> when the content object is
created, so the sources are one click away and the pages carry resolvable citations.
Mentions that are already inside a link, a code span, a preformatted block or a tag
attribute are left alone, as is trailing punctuation.
"""
import html
import re

from pelican import signals

# a DOI starts with 10., a 4-9 digit registrant code and a slash; the suffix runs to the
# next whitespace, tag or quote
DOI_RE = re.compile(r'(?<![\w/"\'>])doi:\s?(10\.\d{4,9}/[^\s<>"\']+)', re.I)
# text that must not be touched: existing links, code, preformatted blocks, and tags
SKIP_RE = re.compile(r"(<a\b.*?</a>|<pre\b.*?</pre>|<code\b.*?</code>|<[^>]*>)", re.S | re.I)
TRAILING = ".,;:"


def _link_match(match):
    doi = match.group(1)
    trailing = ""
    while doi and doi[-1] in TRAILING:
        trailing = doi[-1] + trailing
        doi = doi[:-1]
    # a closing parenthesis belongs to the sentence unless the DOI opened one
    if doi.endswith(")") and doi.count("(") < doi.count(")"):
        trailing = ")" + trailing
        doi = doi[:-1]
    href = html.escape("https://doi.org/" + html.unescape(doi), quote=True)
    return f'<a class="doi" href="{href}">doi:{doi}</a>{trailing}'


def link_dois(text):
    """Return ``text`` with plain DOI mentions linked; see the module docstring."""
    if "doi:" not in text.lower():
        return text
    parts = SKIP_RE.split(text)
    # re.split with one capturing group alternates text and skipped fragments
    return "".join(DOI_RE.sub(_link_match, part) if i % 2 == 0 else part for i, part in enumerate(parts))


def on_content(content):
    body = getattr(content, "_content", None)
    if body:
        content._content = link_dois(body)


def register():
    signals.content_object_init.connect(on_content)
