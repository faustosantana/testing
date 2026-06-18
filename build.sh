#!/usr/bin/env bash
set -euo pipefail

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-build.txt

pyinstaller --onefile --name volume_crypto --console volume_crypto.py

echo "Executable: dist/volume_crypto"
