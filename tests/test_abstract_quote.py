"""The abstract frame of a paper post becomes an attributed quotation, text unchanged."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plugins"))
from mtw_abstract import quote_abstract  # noqa: E402

FRAME = ('<p>Our own paragraph.</p><aside class="m-frame"><h2>Abstract</h2>'
         '<p>We show that X binds Y.</p></aside><p>After.</p>')


def test_abstract_becomes_a_blockquote_that_cites_the_doi():
    out, abstract = quote_abstract(FRAME, doi="10.1000/abc", title="On X and Y",
                                   journal="J. Example", year="2026")
    assert '<section class="paper-abstract"><h2>Abstract of the paper</h2>' in out
    assert '<blockquote cite="https://doi.org/10.1000/abc">' in out
    assert "<p>We show that X binds Y.</p>" in out          # the text itself is untouched
    assert ('<footer>Quoted from <a href="https://doi.org/10.1000/abc"><em>On X and Y</em></a>, '
            "<em>J. Example</em> 2026.</footer>") in out
    assert out.startswith("<p>Our own paragraph.</p>") and out.endswith("<p>After.</p>")
    assert abstract == "We show that X binds Y."


def test_without_a_doi_the_quotation_carries_no_source_line():
    out, abstract = quote_abstract(FRAME)
    assert '<blockquote>' in out and "cite=" not in out and "<footer>" not in out
    assert "<p>We show that X binds Y.</p>" in out
    assert abstract == "We show that X binds Y."


def test_other_frames_and_plain_text_are_left_alone():
    other = '<aside class="m-frame"><h2>Update</h2><p>Now published.</p></aside>'
    out, abstract = quote_abstract(other, doi="10.1000/abc")
    assert out == other and abstract is None
    plain = "<p>No frame here.</p>"
    assert quote_abstract(plain, doi="10.1000/abc") == (plain, None)


def test_only_the_first_abstract_frame_is_rewritten():
    twice = FRAME + FRAME
    out, _ = quote_abstract(twice, doi="10.1000/abc")
    assert out.count("paper-abstract") == 1
    assert out.count('<aside class="m-frame"><h2>Abstract</h2>') == 1


def test_a_creative_commons_licence_is_named_and_linked():
    out, _ = quote_abstract(FRAME, doi="10.1000/abc", title="On X and Y", journal="J. Example",
                            year="2026", license_label="CC BY-NC 4.0")
    assert ('Reproduced under <a href="https://creativecommons.org/licenses/by-nc/4.0/">'
            "CC BY-NC 4.0</a>.</footer>") in out


def test_an_unknown_licence_label_is_printed_but_not_linked():
    out, _ = quote_abstract(FRAME, doi="10.1000/abc", license_label="Publisher licence")
    assert "Reproduced under Publisher licence.</footer>" in out
    assert "creativecommons" not in out


def test_a_post_without_a_licence_claims_none():
    out, _ = quote_abstract(FRAME, doi="10.1000/abc", title="On X and Y")
    assert "Reproduced under" not in out
