"""Mark the paper abstract on a publication post as a quotation.

A publication post reproduces the abstract of the paper verbatim, written in the source as
``.. frame:: Abstract``. Rendered as a plain frame it carries the same typography as the
post itself, so a reader cannot see where the commentary ends and the publisher's text
begins, and a parser has nothing that says whose words these are.

This plugin rewrites that one frame into a labelled quotation: a ``blockquote`` whose
``cite`` is the DOI of the paper, with a footer naming the paper, inside a section that the
stylesheet sets apart from the body text. The abstract text itself is passed through
unchanged, and the plain text is kept on the content object as ``paper_abstract`` so that
the structured data can attach it to the ScholarlyArticle node (the paper) instead of to
the BlogPosting node (the post). Other frames ("Update", "Now published in …") are left
alone.
"""
import html
import re

from pelican import signals

FRAME_RE = re.compile(r'<aside class="m-frame">\s*<h2>Abstract</h2>\s*(?P<body>.*?)</aside>', re.S)
TAG_RE = re.compile(r"<[^>]+>")
# ":paper_license: CC BY 4.0" names the licence of the paper; the deed is linked where the
# label is one of the Creative Commons licences, and printed as given where it is not.
LICENSE_RE = re.compile(r"^CC (BY(?:-NC)?(?:-ND)?(?:-SA)?) (\d\.\d)$")


def _plain(fragment):
    """Tag-free text: tags become a space, so paragraphs do not run into each other."""
    text = html.unescape(re.sub(r"\s+", " ", TAG_RE.sub(" ", fragment)))
    return re.sub(r"\s+([.,;:)])", r"\1", text).strip()


def _license(label):
    """The licence sentence, with a link to the deed for a Creative Commons licence."""
    if not label:
        return ""
    match = LICENSE_RE.match(label.strip())
    shown = html.escape(label.strip())
    if match:
        url = f"https://creativecommons.org/licenses/{match.group(1).lower()}/{match.group(2)}/"
        shown = f'<a href="{html.escape(url, quote=True)}">{shown}</a>'
    return f" Reproduced under {shown}."


def _footer(doi, title, journal, year, license_label=None):
    """One line naming the quoted paper, so the quotation stands on its own."""
    if not doi:
        return ""
    url = html.escape("https://doi.org/" + doi, quote=True)
    name = f"<em>{html.escape(title)}</em>" if title else "the paper"
    where = f", <em>{html.escape(journal)}</em>" if journal else ""
    when = f" {html.escape(str(year))}" if year else ""
    return (f'<footer>Quoted from <a href="{url}">{name}</a>{where}{when}.'
            f'{_license(license_label)}</footer>')


def quote_abstract(text, doi=None, title=None, journal=None, year=None, license_label=None):
    """Return ``text`` with the abstract frame rewritten as an attributed quotation."""
    if "<h2>Abstract</h2>" not in text:
        return text, None
    abstract = {"plain": None}

    def replace(match):
        body = match.group("body").strip()
        abstract["plain"] = _plain(body)
        cite = f' cite="{html.escape("https://doi.org/" + doi, quote=True)}"' if doi else ""
        return ('<section class="paper-abstract"><h2>Abstract of the paper</h2>'
                f'<blockquote{cite}>{body}'
                f'{_footer(doi, title, journal, year, license_label)}</blockquote></section>')

    return FRAME_RE.sub(replace, text, count=1), abstract["plain"]


def on_content(content):
    body = getattr(content, "_content", None)
    if not body:
        return
    rewritten, abstract = quote_abstract(
        body,
        doi=getattr(content, "doi", None),
        title=getattr(content, "paper_title", None),
        journal=getattr(content, "journal", None),
        year=getattr(content, "year", None),
        license_label=getattr(content, "paper_license", None),
    )
    if abstract:
        content._content = rewritten
        content.paper_abstract = abstract


def register():
    signals.content_object_init.connect(on_content)
