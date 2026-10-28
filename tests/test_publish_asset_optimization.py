import subprocess
import sys


def test_publish_asset_optimizer_minifies_css_js_and_html(tmp_path):
    output_dir = tmp_path / "output"
    output_static_dir = output_dir / "static"
    output_static_dir.mkdir(parents=True)

    css_source = "/* comment */\nbody { color: red; }\n"
    js_source = "function test() {   return 1 + 2; }\n"
    html_source = (
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head><style>body { color: blue; }</style></head>\n"
        "<body><script>function demo () { return 1 + 1; }</script></body>\n"
        "</html>\n"
    )
    (output_static_dir / "site.css").write_text(css_source, encoding="utf-8")
    (output_static_dir / "site.js").write_text(js_source, encoding="utf-8")
    (output_dir / "index.html").write_text(html_source, encoding="utf-8")

    subprocess.run([sys.executable, "scripts/optimize_publish.py", str(output_dir)], check=True)

    minified_css = (output_static_dir / "site.css").read_text(encoding="utf-8")
    minified_js = (output_static_dir / "site.js").read_text(encoding="utf-8")
    minified_html = (output_dir / "index.html").read_text(encoding="utf-8")

    # Properties rather than byte-exact output: the minifiers are not pinned.
    assert "comment" not in minified_css and "\n" not in minified_css
    assert "color:red" in minified_css.replace(" ", "")
    assert len(minified_js) < len(js_source) and "return" in minified_js
    assert len(minified_html) < len(html_source) and "\n" not in minified_html
    assert "<script>" in minified_html and "demo" in minified_html


def test_publish_asset_optimizer_keeps_meta_tags_in_conventional_form(tmp_path):
    # LinkedIn's scraper found no Open Graph tags in <meta content=... property=og:image>
    # (sorted, unquoted attributes as the minifier emits them). Published pages must carry
    # the conventional <meta property="..." content="..."> form.
    output_dir = tmp_path / "output"
    output_dir.mkdir(parents=True)
    html_source = (
        "<!DOCTYPE html><html><head>"
        '<meta charset="UTF-8" />'
        '<meta name="description" content="A page" />'
        '<meta property="og:image" content="https://example.org/static/card.png" />'
        '<meta property="og:title" content="Title with &quot;quotes&quot; and spaces" />'
        '<meta content="1200" property="og:image:width" />'
        "</head><body></body></html>"
    )
    (output_dir / "index.html").write_text(html_source, encoding="utf-8")

    subprocess.run([sys.executable, "scripts/optimize_publish.py", str(output_dir)], check=True)

    minified_html = (output_dir / "index.html").read_text(encoding="utf-8")
    assert '<meta property="og:image" content="https://example.org/static/card.png">' in minified_html
    assert '<meta property="og:image:width" content="1200">' in minified_html
    assert '<meta name="description" content="A page">' in minified_html
    assert '<meta property="og:title" content="Title with &quot;quotes&quot; and spaces">' in minified_html
    assert '<meta charset="UTF-8">' in minified_html
