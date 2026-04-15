import subprocess
import sys


def test_publish_asset_optimizer_minifies_css_js_and_html(tmp_path):
    static_dir = tmp_path / "static"
    output_dir = tmp_path / "output"
    output_static_dir = output_dir / "static"
    static_dir.mkdir(parents=True)
    output_static_dir.mkdir(parents=True)

    (static_dir / "postprocess.py").write_text(
        "#!/usr/bin/env python3\n"
        "import pathlib\n"
        "import sys\n"
        "source = pathlib.Path(sys.argv[1])\n"
        "target = pathlib.Path(sys.argv[sys.argv.index('-o') + 1])\n"
        "target.write_text(source.read_text(), encoding='utf-8')\n",
        encoding="utf-8",
    )
    (static_dir / "m-light.css").write_text(
        "/* theme */\nbody { color: black; }\n",
        encoding="utf-8",
    )
    (output_static_dir / "site.css").write_text(
        "/* comment */\nbody { color: red; }\n",
        encoding="utf-8",
    )
    (output_static_dir / "site.js").write_text(
        "function test() {   return 1 + 2; }\n",
        encoding="utf-8",
    )
    (output_dir / "index.html").write_text(
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head><style>body { color: blue; }</style></head>\n"
        "<body><script>function demo () { return 1 + 1; }</script></body>\n"
        "</html>\n",
        encoding="utf-8",
    )

    subprocess.run(
        [
            sys.executable,
            "scripts/optimize_publish.py",
            str(output_dir),
            "--source-static-dir",
            str(static_dir),
        ],
        check=True,
    )

    compiled_css = (output_static_dir / "m-light.compiled.css").read_text(encoding="utf-8")
    minified_css = (output_static_dir / "site.css").read_text(encoding="utf-8")
    minified_js = (output_static_dir / "site.js").read_text(encoding="utf-8")
    minified_html = (output_dir / "index.html").read_text(encoding="utf-8")

    assert "color:black" in compiled_css
    assert "comment" not in minified_css
    assert "\n" not in minified_css
    assert "function test(){return 1+2;}" == minified_js
    assert "\n" not in minified_html
    assert "<script>function demo(){return 2}</script>" in minified_html
