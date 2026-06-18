#!/usr/bin/env bash
set -euo pipefail

pip install pyinstaller

pyinstaller --onefile --name volume_crypto volume_crypto.py
