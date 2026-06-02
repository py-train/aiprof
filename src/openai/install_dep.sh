#!/usr/bin/env bash
set -e

# Upgrade pip and install required packages.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo ""
echo "Installation complete."
