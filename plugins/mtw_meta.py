"""Site-specific metadata derived at build time.

* Talk and poster pages: the rendered line blocks are parsed into ``page.events`` (title,
  venue, place, date, PDF, DOI, label) so that the structured data can list them as Events.
* Pages without an explicit ``:modified:`` get the date of their last git commit, so that
  ``dateModified`` and the sitemap ``lastmod`` do not fall back to the build time. The
  deploy workflow checks out the full history for this.
"""
import html
import re
import subprocess
from datetime import datetime
from pathlib import Path

from pelican import signals
from pelican.contents import Page

EVENT_PAGES = {"publications/presentations": "talk", "publications/posters": "poster"}
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], 1)}
DATE_RE = re.compile(r"(?:(\d{1,2})\s+)?(" + "|".join(MONTHS) + r")\s+(\d{4})", re.I)
TAG_RE = re.compile(r"<[^>]+>")
_git_dates = {}


def _text(fragment):
    return html.unescape(re.sub(r"\s+", " ", TAG_RE.sub("", fragment))).strip()


def _events(content, kind):
    events = []
    for para in re.findall(r"<p\b[^>]*>(.*?)</p>", content, re.S):
        raw_lines = [l for l in re.split(r"<br\s*/?>", para) if _text(l)]
        lines = [_text(l) for l in raw_lines]
        venue_idx = next((i for i, l in enumerate(lines) if l.startswith("Presented at")), None)
        if venue_idx is None or venue_idx + 1 >= len(lines):
            continue
        where = lines[venue_idx + 1]
        date = DATE_RE.search(where)
        if not date:
            continue
        day, month, year = date.groups()
        event = {
            "name": lines[0],
            "venue": re.sub(r"^Presented at (the )?", "", lines[venue_idx]),
            "place": where[: date.start()].strip(" .,"),
            "date": f"{year}-{MONTHS[month.lower()]:02d}" + (f"-{int(day):02d}" if day else ""),
            "kind": kind,
        }
        pdf = re.search(r'href="([^"]+\.pdf)"', raw_lines[0])
        if pdf:
            # {static} links are only resolved when the page is written; the site-absolute path is enough here
            event["pdf"] = pdf.group(1).replace("{static}", "")
        doi = re.search(r"doi\.org/([^\"'<\s]+)", para)
        if doi:
            event["doi"] = doi.group(1)
        label = re.search(r'class="m-label[^"]*">([^<]+)<', para)
        if label:
            event["label"] = label.group(1).strip()
        if kind == "poster" and venue_idx >= 2:
            event["authors"] = lines[1]
        events.append(event)
    return events


def _git_modified(path):
    path = Path(path)
    if path in _git_dates:
        return _git_dates[path]
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cI", "--", path.name],
                             cwd=path.parent, capture_output=True, text=True, check=True).stdout.strip()
        value = datetime.fromisoformat(out) if out else None
    except (OSError, subprocess.CalledProcessError, ValueError):
        value = None
    _git_dates[path] = value
    return value


def on_content(content):
    if not isinstance(content, Page):
        return
    kind = EVENT_PAGES.get(getattr(content, "slug", ""))
    if kind and content._content:
        content.events = _events(content._content, kind)
    if not hasattr(content, "modified") and getattr(content, "source_path", None):
        modified = _git_modified(content.source_path)
        if modified:
            content.modified = modified


def register():
    signals.content_object_init.connect(on_content)
