"""The commands and config in the how-to posts are syntactically valid and current.

Nothing here proves that `codex --oss` drives a model correctly: that needs a 13 GB
download and minutes of GPU time, and it belongs in a manual re-run before publishing an
update, not in a test suite. What is checked:

Always (offline, no tools needed)
  - every ``toml`` block parses, and its keys exist in the tool it configures
  - every ``json`` block parses
  - every ``bash`` block is valid shell syntax
  - the shell lines invoke only commands the posts have introduced

Opt-in with CHECK_AI_COMMANDS=1 (needs the tools installed)
  - the flags and subcommands the posts use are in the tools' own --help
  - the versions the posts claim to have been run with are not newer than what is
    installed, which catches a quoted version that was never true
  - a version that has moved on is reported, so the post can be re-run and re-dated

Opt-in with CHECK_AI_MODELS=1 (needs the network)
  - the model identifiers the posts name still exist upstream
"""
import json
import os
import re
import shutil
import subprocess
import tomllib
from pathlib import Path

import pytest

BLOG = Path(__file__).resolve().parents[1] / "content" / "blog"
AI_SLUGS = ("claude-code", "codex", "ollama", "local-llm", "lm-studio", "apple-silicon", "qwen")

# Keys Codex reads from ~/.codex/config.toml, as used by the posts. A typo in one of
# these is silently ignored by Codex, which is exactly the failure a reader cannot debug.
CODEX_KEYS = {
    "oss_provider", "model", "model_context_window", "model_provider", "model_reasoning_effort",
    "approval_policy", "sandbox_mode", "model_max_output_tokens", "disable_response_storage",
    "name", "base_url", "wire_api", "env_key", "query_params", "http_headers", "request_max_retries",
    "stream_max_retries", "stream_idle_timeout_ms",
}
CODEX_TABLES = ("model_providers", "profiles", "mcp_servers", "sandbox_workspace_write", "tools",
                "shell_environment_policy", "history", "tui")

# Commands the posts introduce, plus the shell builtins and coreutils they lean on.
KNOWN_COMMANDS = {
    "ollama", "lms", "codex", "claude", "exo", "brew", "uv", "npm", "git", "nix",
    "curl", "export", "cd", "sudo", "python3", "pip", "sed", "cat", "head", "tail",
    "echo", "systemctl", "launchctl", "jq", "set", "source", "mkdir", "cp", "mv", "rm",
    "printf", "grep", "awk", "sort", "uniq", "wc", "test", "open", "defaults", "killall",
}


def ai_posts():
    return sorted(p for p in BLOG.glob("*.rst") if any(k in p.name.lower() for k in AI_SLUGS))


def blocks(text, lang):
    """Every ``.. code-block:: <lang>`` body, dedented."""
    out = []
    pattern = re.compile(rf"\.\. code-block:: {lang}\n(?:\s+:[\w-]+:.*\n)*\n((?:(?:[ \t]+.*)?\n)+)")
    for m in pattern.finditer(text):
        body = m.group(1)
        lines = [ln for ln in body.splitlines() if ln.strip()]
        if not lines:
            continue
        indent = min(len(ln) - len(ln.lstrip()) for ln in lines)
        out.append("\n".join(ln[indent:] if len(ln) >= indent else ln for ln in body.splitlines()))
    return out


def test_ai_posts_are_found():
    assert len(ai_posts()) >= 4


@pytest.mark.parametrize("post", ai_posts(), ids=lambda p: p.name)
def test_toml_blocks_parse_and_use_known_keys(post):
    for i, body in enumerate(blocks(post.read_text(encoding="utf-8"), "toml"), 1):
        # Comments after a value are fine; tomllib handles them.
        try:
            data = tomllib.loads(body)
        except tomllib.TOMLDecodeError as e:
            pytest.fail(f"{post.name}: toml block {i} does not parse: {e}\n{body}")
        stack = [("", data)]
        while stack:
            prefix, node = stack.pop()
            for key, value in node.items():
                if isinstance(value, dict):
                    top = (prefix or key).split(".")[0]
                    assert top in CODEX_TABLES or prefix, (
                        f"{post.name}: toml block {i} has unknown table [{prefix or key}]")
                    stack.append((f"{prefix}.{key}" if prefix else key, value))
                else:
                    assert key in CODEX_KEYS, (
                        f"{post.name}: toml block {i} sets unknown key {key!r} "
                        f"(in [{prefix}])" if prefix else
                        f"{post.name}: toml block {i} sets unknown key {key!r}")


@pytest.mark.parametrize("post", ai_posts(), ids=lambda p: p.name)
def test_json_blocks_parse(post):
    for i, body in enumerate(blocks(post.read_text(encoding="utf-8"), "json"), 1):
        try:
            json.loads(body)
        except json.JSONDecodeError as e:
            pytest.fail(f"{post.name}: json block {i} does not parse: {e}\n{body}")


@pytest.mark.parametrize("post", ai_posts(), ids=lambda p: p.name)
def test_bash_blocks_are_valid_shell(post):
    for i, body in enumerate(blocks(post.read_text(encoding="utf-8"), "bash"), 1):
        r = subprocess.run(["bash", "-n"], input=body, text=True, capture_output=True)
        assert r.returncode == 0, f"{post.name}: bash block {i} is not valid shell:\n{r.stderr}\n{body}"


@pytest.mark.parametrize("post", ai_posts(), ids=lambda p: p.name)
def test_shell_blocks_invoke_known_commands(post):
    for i, body in enumerate(blocks(post.read_text(encoding="utf-8"), "bash"), 1):
        for line in body.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Continuations, redirections, here-doc bodies and quoted JSON payloads are
            # not command positions.
            if line.startswith(("-", '"', "'", ">", "|", ")", "}", "EOF")):
                continue
            first = line.split()[0].lstrip("$(").rstrip(")")
            if "=" in first and not first.startswith("-"):      # VAR=value prefix
                parts = line.split()
                first = next((p for p in parts if "=" not in p), first)
            first = first.lstrip("$(")
            if not first or not re.match(r"^[A-Za-z_][\w.-]*$", first):
                continue
            assert first in KNOWN_COMMANDS, (
                f"{post.name}: bash block {i} runs {first!r}, which the post never "
                f"introduces and the test does not know. Add it to KNOWN_COMMANDS if "
                f"it is deliberate.\n    {line}")


# --- opt-in: the tools themselves -------------------------------------------------

needs_tools = pytest.mark.skipif(not os.environ.get("CHECK_AI_COMMANDS"),
                                 reason="set CHECK_AI_COMMANDS=1")

# Flag or subcommand -> the command whose --help must mention it.
USAGE = [
    ("codex", "--oss"), ("codex", "--profile"), ("codex", "exec"),
    ("ollama", "ps"), ("ollama", "pull"), ("ollama", "serve"),
    ("lms", "ps"), ("lms", "get"), ("lms", "load"),
]


@needs_tools
@pytest.mark.parametrize("tool,flag", USAGE, ids=lambda x: str(x))
def test_documented_flags_still_exist(tool, flag):
    if not shutil.which(tool):
        pytest.skip(f"{tool} is not installed")
    text = ""
    for args in ([tool, "--help"], [tool, "help"], [tool, flag, "--help"]):
        r = subprocess.run(args, capture_output=True, text=True, timeout=60)
        text += r.stdout + r.stderr
    assert flag in text, f"`{tool} {flag}` is used in a post but is not in {tool}'s help output"


# What each post says it was run with: post name -> {tool: version}
CLAIMED = {
    "2026-09-24-codex-cli-local-model-lm-studio-ollama.rst": {"codex": "0.163", "ollama": "0.40"},
    "2026-09-24-run-claude-code-with-ollama.rst": {"claude": "2.1.302", "ollama": "0.40"},
    "2026-10-28-claude-code-csv-reproducible-analysis.rst": {"claude": "2.1.310", "ollama": "0.40.2"},
    "2026-04-17-run-claude-code-with-local-llm-macos-qwen3.rst": {"claude": "2.1.302"},
}
VERSION_CMD = {"codex": ["codex", "--version"], "ollama": ["ollama", "--version"],
               "claude": ["claude", "--version"], "lms": ["lms", "version"]}


def _installed(tool):
    r = subprocess.run(VERSION_CMD[tool], capture_output=True, text=True, timeout=60)
    m = re.search(r"(\d+\.\d+(?:\.\d+)?)", r.stdout + r.stderr)
    return m.group(1) if m else None


def _tuple(v):
    return tuple(int(x) for x in v.split("."))


@needs_tools
@pytest.mark.parametrize("post,claims", sorted(CLAIMED.items()), ids=lambda x: x if isinstance(x, str) else "")
def test_claimed_versions_are_not_from_the_future(post, claims):
    """A post may quote an older version than the one installed, which only means it is
    due a re-run. It must never quote a version that does not exist yet."""
    assert (BLOG / post).exists(), f"{post} was renamed; update CLAIMED"
    for tool, claimed in claims.items():
        if not shutil.which(tool):
            pytest.skip(f"{tool} is not installed")
        got = _installed(tool)
        if got is None:
            pytest.skip(f"cannot read {tool}'s version")
        assert _tuple(claimed) <= _tuple(got), (
            f"{post} says it was run with {tool} {claimed}, but only {got} is installed, "
            f"so the claim cannot be true")


@needs_tools
def test_report_tools_that_have_moved_on(record_property):
    """Not a failure: a post quoting an older version is a signal to re-run it."""
    stale = []
    for post, claims in sorted(CLAIMED.items()):
        for tool, claimed in claims.items():
            if not shutil.which(tool):
                continue
            got = _installed(tool)
            if got and _tuple(claimed) < _tuple(got):
                stale.append(f"{post}: {tool} {claimed} -> {got}")
    record_property("stale_versions", "; ".join(stale))
    if stale:
        print("\nposts due a re-run because the tool has moved on:")
        for s in stale:
            print("   ", s)


# --- opt-in: the model identifiers ------------------------------------------------

needs_net = pytest.mark.skipif(not os.environ.get("CHECK_AI_MODELS"), reason="set CHECK_AI_MODELS=1")

OLLAMA_MODELS = ["gpt-oss:20b", "gpt-oss:120b", "qwen3-coder:30b"]
HF_MODELS = ["openai/gpt-oss-20b", "google/gemma-4-12b"]


@needs_net
@pytest.mark.parametrize("model", OLLAMA_MODELS)
def test_ollama_models_exist(model):
    import urllib.error
    import urllib.request
    name = model.split(":")[0]
    url = f"https://ollama.com/library/{name}"
    try:
        with urllib.request.urlopen(urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0 (compatible; link-check)"}), timeout=30) as r:
            assert r.status == 200
    except urllib.error.HTTPError as e:
        pytest.fail(f"{model} is named in a post but {url} answers {e.code}")


@needs_net
@pytest.mark.parametrize("model", HF_MODELS)
def test_huggingface_models_exist(model):
    import urllib.error
    import urllib.request
    url = f"https://huggingface.co/api/models/{model}"
    try:
        with urllib.request.urlopen(urllib.request.Request(
                url, headers={"User-Agent": "link-check"}), timeout=30) as r:
            assert json.load(r).get("id", "").lower() == model.lower()
    except urllib.error.HTTPError as e:
        pytest.fail(f"{model} is named in a post but the HF API answers {e.code}")
