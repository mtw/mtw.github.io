#!/usr/bin/env python3
"""
Blog split migration for the relaunch2026 branch.

Run from the Pelican/ directory:

    python3 tools/split_blog.py --dry-run
    python3 tools/split_blog.py

What it does (all edits are metadata-only; no file is renamed, no slug changes,
so every article and page URL stays exactly as it is today):

  1. Adds a ":section:" field to the 14 non-publication posts so the blog index
     can group them into Guides / Essays / Talks & events. Pelican does not
     generate pages from arbitrary metadata, so this adds no URLs.

  2. Normalises the ":category: HOWTO" duplicate to "howto". This is the ONE
     intentional URL change in the whole migration: it removes
     /blog/category/HOWTO.html. The post itself keeps its URL.

  3. Adds ":canonical_url:" to the six /publications/papers/ stub pages, each
     pointing at the blog post that already holds the content. The stubs stay
     live; Google consolidates ranking signal onto the canonical post.

  4. Strips the per-paper PDF links from content/publications.rst, leaving DOI, the external
     publisher link, and the label. Every entry there already links to its blog post, so the
     index becomes a directory of canonical pages instead of a third copy of each paper.
     PDFs stay at their current paths and remain linked from the canonical blog post.
     The aggregate "publication list as PDF" link at the top of the page is kept -- it is a
     CV-style summary, not a competitor to any individual paper page.

Idempotent: re-running makes no further changes.
"""

import argparse
import pathlib
import re
import sys

BLOG = pathlib.Path("content/blog")
PAPERS = pathlib.Path("content/publications/papers")
PUBLICATIONS = pathlib.Path("content/publications.rst")

# Per-paper asset links removed from the publications index. All four are PDFs and all four
# competed with the canonical blog post for the same query.
PDF_LABELS = ("Preprint PDF", "PDF", "Figures", "Supplement")
PDF_SEGMENT_RE = re.compile(
    r"\s*\|\s*:link-flat:`(?:" + "|".join(re.escape(l) for l in PDF_LABELS) + r")\s*<\{static\}[^`]*?>`"
)

# ---------------------------------------------------------------- 1. sections

SECTIONS = {
    "guides": [
        "2014-04-15-how-to-compute-normalized-rna-seq-expression-from-multicov-files",
        "2022-10-20-When-SHAPE-Data-Actually-Improves-RNA-Structure-Prediction",
        "2026-03-01-When-to-Trust-RNA-Structure-Prediction-for-Experimental-Decisions",
        "2026-03-15-How-to-Review-an-RNA-Design-Before-Synthesis",
        "2026-04-05-When-Sequence-Conservation-Is-Not-Enough-to-Find-Functional-RNA-Structure",
        "2026-04-17-run-claude-code-with-local-llm-macos-qwen3",
        "2026-05-09-How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions",
    ],
    "essays": [
        "2022-11-18-The-link-between-mRNA-vaccine-design-and-barbeque-optimization",
        "2025-01-20-Why-Kinetic-Folding-Matters-in-RNA-Design",
        "2025-02-01-What-AI-Can-and-Cannot-Do-for-RNA-Structure-and-RNA-Protein-Modeling",
        "2026-03-22-What-AI-Is-Genuinely-Useful-for-in-RNA-Biology",
    ],
    "talks": [
        "2023-11-03-Virus_Bioinformatics_and_Health_Day",
        "2025-07-18-Exploring-RNA-Biology-with-Deep-Learning",
        "2025-07-29-Functional-RNAs-in-Virology",
    ],
}

CATEGORY_RE = re.compile(r"^:category:\s*(.+?)\s*$", re.MULTILINE)
SECTION_RE = re.compile(r"^:section:\s*(.+?)\s*$", re.MULTILINE)
CANONICAL_RE = re.compile(r"^:canonical_url:\s*(.+?)\s*$", re.MULTILINE)
FILENAME_REF_RE = re.compile(r"\{filename\}/blog/(?P<name>[^<>`\s]+?)\.rst")


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text, dry_run):
    if dry_run:
        return
    path.write_text(text, encoding="utf-8")


def insert_after_category(text, line):
    """Insert `line` directly after the :category: field, preserving indentation."""
    m = CATEGORY_RE.search(text)
    if not m:
        return None
    end = m.end()
    return text[:end] + "\n" + line + text[end:]


def do_sections(dry_run):
    changed = skipped = missing = 0
    for section, slugs in SECTIONS.items():
        for slug in slugs:
            path = BLOG / f"{slug}.rst"
            if not path.exists():
                print(f"  MISSING  {path}")
                missing += 1
                continue
            text = read(path)
            existing = SECTION_RE.search(text)
            if existing:
                if existing.group(1) == section:
                    skipped += 1
                    continue
                text = SECTION_RE.sub(f":section: {section}", text, count=1)
            else:
                updated = insert_after_category(text, f":section: {section}")
                if updated is None:
                    print(f"  NO :category: FIELD  {path}")
                    missing += 1
                    continue
                text = updated
            write(path, text, dry_run)
            print(f"  section={section:7s} {path.name}")
            changed += 1
    print(f"  -> {changed} set, {skipped} already correct, {missing} problem(s)")
    return missing


def do_category_case(dry_run):
    changed = 0
    for path in sorted(BLOG.glob("*.rst")):
        text = read(path)
        m = CATEGORY_RE.search(text)
        if not m or m.group(1) != "HOWTO":
            continue
        text = CATEGORY_RE.sub(":category: howto", text, count=1)
        write(path, text, dry_run)
        print(f"  HOWTO -> howto  {path.name}")
        changed += 1
    print(f"  -> {changed} file(s) normalised")
    return 0


def do_canonicals(dry_run):
    changed = skipped = problems = 0
    for path in sorted(PAPERS.glob("*.rst")):
        text = read(path)
        if CANONICAL_RE.search(text):
            skipped += 1
            continue
        ref = FILENAME_REF_RE.search(text)
        if not ref:
            print(f"  NO BLOG REFERENCE  {path.name}")
            problems += 1
            continue
        name = ref.group("name")
        year = name[:4]
        if not year.isdigit():
            print(f"  CANNOT DERIVE YEAR  {path.name} -> {name}")
            problems += 1
            continue
        canonical = f"https://michaelwolfinger.com/blog/{year}/{name}/"
        # place the canonical right after the :description: line, or the title block
        anchor = re.search(r"^:description:.*$", text, re.MULTILINE)
        if anchor:
            end = anchor.end()
            text = text[:end] + f"\n:canonical_url: {canonical}" + text[end:]
        else:
            anchor = re.search(r"^:title:.*$", text, re.MULTILINE)
            if not anchor:
                print(f"  NO :title:/:description: ANCHOR  {path.name}")
                problems += 1
                continue
            end = anchor.end()
            text = text[:end] + f"\n:canonical_url: {canonical}" + text[end:]
        write(path, text, dry_run)
        print(f"  canonical  {path.name}\n             -> {canonical}")
        changed += 1
    print(f"  -> {changed} set, {skipped} already had one, {problems} problem(s)")
    return problems


def do_publication_pdf_links(dry_run):
    if not PUBLICATIONS.exists():
        print(f"  MISSING  {PUBLICATIONS}")
        return 1
    text = read(PUBLICATIONS)
    removed = 0
    out = []
    for line in text.splitlines(keepends=True):
        # Only touch a paper's link line. Every entry ends its link line with the type label,
        # which keeps this away from prose, figures, and the aggregate publication-list PDF.
        if ":label-flat-info:" not in line:
            out.append(line)
            continue
        new_line, n = PDF_SEGMENT_RE.subn("", line)
        removed += n
        out.append(new_line)
    if not removed:
        print("  -> no PDF links found (already applied)")
        return 0
    write(PUBLICATIONS, "".join(out), dry_run)
    print(f"  -> {removed} per-paper PDF link(s) removed from {PUBLICATIONS.name}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    args = ap.parse_args()

    if not BLOG.is_dir() or not PAPERS.is_dir():
        sys.exit("Run this from the Pelican/ directory (content/blog must exist).")

    if args.dry_run:
        print("DRY RUN — no files will be written\n")

    problems = 0
    print("1. Section metadata on non-publication posts")
    problems += do_sections(args.dry_run)
    print("\n2. Category case normalisation (HOWTO -> howto)")
    problems += do_category_case(args.dry_run)
    print("\n3. Canonical URLs on /publications/papers/ stubs")
    problems += do_canonicals(args.dry_run)
    print("\n4. Per-paper PDF links in publications.rst")
    problems += do_publication_pdf_links(args.dry_run)

    print("\nDone." if not problems else f"\nDone with {problems} problem(s) — review above.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
