#!/usr/bin/env sh
set -eu

repo_root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$repo_root"

rm -rf \
  .pytest_cache \
  .ruff_cache \
  michaelwolfinger_com.egg-info \
  output \
  output-publish \
  plugins/m/__pycache__ \
  tests/__pycache__

find . \
  \( -path './.git' -o -path './.venv' \) -prune -o \
  \( -name '.DS_Store' -o -name '__pycache__' -o -name '*~' \) \
  -exec rm -rf {} +
