"""The DOI plugin links plain ``doi:`` mentions and leaves everything else alone."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plugins"))
from mtw_doi import link_dois  # noqa: E402


def test_plain_doi_becomes_a_link_and_keeps_the_sentence_punctuation():
    out = link_dois("<p>Methods 103:86–98 (2016). doi:10.1016/j.ymeth.2016.04.004. On this site.</p>")
    assert out == ('<p>Methods 103:86–98 (2016). <a class="doi" href="https://doi.org/10.1016/j.ymeth.2016.04.004">'
                   'doi:10.1016/j.ymeth.2016.04.004</a>. On this site.</p>')


def test_semicolon_space_and_parenthesis_are_not_part_of_the_doi():
    assert link_dois("(doi: 10.4161/rna.24971); next") == \
        '(<a class="doi" href="https://doi.org/10.4161/rna.24971">doi:10.4161/rna.24971</a>); next'
    assert link_dois("see doi:10.1002/(SICI)1097-0282 here") == \
        'see <a class="doi" href="https://doi.org/10.1002/(SICI)1097-0282">doi:10.1002/(SICI)1097-0282</a> here'


def test_existing_links_code_and_attributes_are_left_alone():
    already = '<a href="https://doi.org/10.1/x">doi:10.1/x</a>'
    assert link_dois(already) == already
    code = "<code>doi:10.1000/abc</code> and <pre>\ndoi:10.1000/abc\n</pre>"
    assert link_dois(code) == code
    attr = '<img alt="doi:10.1000/abc" src="x.png">'
    assert link_dois(attr) == attr
    assert link_dois("https://doi.org/10.1000/abc") == "https://doi.org/10.1000/abc"


def test_text_without_dois_is_returned_unchanged():
    text = "<p>No identifiers here.</p>"
    assert link_dois(text) is text
