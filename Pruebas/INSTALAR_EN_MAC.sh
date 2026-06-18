#!/bin/bash
set -euo pipefail

TARGET="/Users/faustosantana/Pruebas"
SOURCE="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$TARGET"

cp "$SOURCE/volume_crypto.py" "$TARGET/"
cp "$SOURCE/COMPILAR.bat" "$TARGET/"
cp "$SOURCE/LEEME.txt" "$TARGET/"
cp "$SOURCE/requirements-build.txt" "$TARGET/"

echo "Archivos copiados en: $TARGET"
echo "Abre esa carpeta en Finder."
open "$TARGET"
