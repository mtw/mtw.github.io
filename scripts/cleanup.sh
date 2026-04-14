#!/usr/bin/env sh
set -eu

repo_root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$repo_root"

rm -rf \
  .pytest_cache \
  .ruff_cache \
  michaelwolfinger_com.egg-info \
  Pelican/output \
  Pelican/.pytest_cache \
  Pelican/__pycache__ \
  Pelican/tests/__pycache__ \
  Pelican/plugins/m/__pycache__ \
  Pelican/pelican-theme/test/__pycache__ \
  tests/__pycache__

find . \
  \( -path './.git' -o -path './.venv' \) -prune -o \
  \( -name '.DS_Store' -o -name '__pycache__' -o -name '*~' \) \
  -exec rm -rf {} +
