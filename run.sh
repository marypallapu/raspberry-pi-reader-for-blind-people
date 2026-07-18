#!/usr/bin/env bash
#
# Raspberry Pi Based Reader for Blind People
#
# Installs the required Python dependencies (if needed)
# and launches the main application.
#

set -euo pipefail

cd "$(dirname "$0")"

echo "==> Raspberry Pi Based Reader for Blind People"

echo "==> Checking Python installation"
python3 --version

echo
echo "==> Installing required Python packages"
pip3 install -r requirements.txt

echo
echo "==> Creating images directory"
mkdir -p images

echo
echo "==> Starting Raspberry Pi Reader Application"
python3 main.py

echo
echo "==> Application terminated"
