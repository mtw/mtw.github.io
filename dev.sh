#!/usr/bin/env sh
# Development server from the repository root. Pelican only finds its settings when run
# inside Pelican/, so this changes into that folder and runs the autoreloading server:
#   ./dev.sh                  build, serve on http://127.0.0.1:8000, rebuild on change
#   ./dev.sh publishconf.py   the same with the production settings
# Any further arguments are passed to pelican (e.g. ./dev.sh pelicanconf.py -p 8001).
set -eu
root="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
settings="${1:-pelicanconf.py}"; [ $# -gt 0 ] && shift
if [ -x "$root/.venv/bin/pelican" ]; then pelican="$root/.venv/bin/pelican"
elif command -v pelican >/dev/null 2>&1; then pelican=pelican
else echo "error: pelican not found; create the venv first (see README)" >&2; exit 127; fi
cd "$root/Pelican"
exec "$pelican" content -lr -d -o output -s "$settings" "$@"
