#!/usr/bin/env sh
set -eu

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
repo_root="$(CDPATH= cd -- "$script_dir/.." && pwd)"

if [ -x "$repo_root/.venv/bin/pelican" ]; then
  pelican="$repo_root/.venv/bin/pelican"
elif command -v pelican >/dev/null 2>&1; then
  pelican="pelican"
else
  echo "error: pelican not found. Activate the venv or install requirements." >&2
  echo "hint: source \"$repo_root/.venv/bin/activate\" && \"$0\"" >&2
  exit 127
fi

cd "$script_dir"
"$pelican" content -D -vv -o output -s pelicanconf.py
"$pelican" content -D -vv -o output -s publishconf.py
