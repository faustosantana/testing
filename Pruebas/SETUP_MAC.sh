#!/bin/bash
set -euo pipefail

TARGET="/Users/faustosantana/Pruebas"

mkdir -p "$TARGET"

cat > "$TARGET/volume_crypto.py" <<'PYEOF'
#!/usr/bin/env python3

import argparse
import ctypes
import os
import subprocess
import sys

KEY = r"Q|&-aVITR856TX>,'^\7~kQ0j\_7Dp~6doMN5hQ:u084Y>"
KEY_FILE = "key.bin"


class VolumeCryptoError(Exception):
    pass


def is_admin() -> bool:
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except (AttributeError, OSError):
        return False


def require_windows() -> None:
    if os.name != "nt":
        raise VolumeCryptoError("this utility requires Windows")


def normalize_drive(drive: str) -> str:
    value = drive.strip().upper()
    if len(value) == 1 and value.isalpha():
        return f"{value}:"
    if len(value) == 2 and value[0].isalpha() and value.endswith(":"):
        return value
    raise VolumeCryptoError(f"invalid drive letter: {drive}")


def write_key(path: str) -> str:
    absolute = os.path.abspath(path)
    with open(absolute, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(KEY)
    return absolute


def resolve_key_path(path: str) -> str:
    absolute = os.path.abspath(path)
    if not os.path.isfile(absolute):
        raise VolumeCryptoError(f"key file not found: {absolute}")
    return absolute


def run_manage_bde(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["manage-bde", *arguments],
        capture_output=True,
        text=True,
        check=False,
    )


def encrypt_drive(drive: str) -> int:
    key_path = write_key(KEY_FILE)
    result = run_manage_bde(["-on", drive, "-RecoveryKey", key_path])
    if result.returncode != 0:
        print('Error: Operation failed. Please contact system administrator.')
        return 1
    print("success: volume encrypted")
    print(f"key: {key_path}")
    return 0


def decrypt_drive(drive: str, key_path: str) -> int:
    resolved_key = resolve_key_path(key_path)
    result = run_manage_bde(["-unlock", drive, "-RecoveryKey", resolved_key])
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise VolumeCryptoError(detail or "decryption failed")
    print("success: volume decrypted")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt", metavar="letra_unidad")
    group.add_argument("--decrypt", metavar="letra_unidad")
    parser.add_argument("--key", metavar="file", default=KEY_FILE)
    return parser


def main(argv: list[str] | None = None) -> int:
    if not is_admin():
        print("error: administrator privileges required", file=sys.stderr)
        return 1

    try:
        require_windows()
    except VolumeCryptoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        drive = normalize_drive(args.encrypt or args.decrypt)
    except VolumeCryptoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.encrypt is not None:
        return encrypt_drive(drive)

    try:
        return decrypt_drive(drive, args.key)
    except VolumeCryptoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
PYEOF

cat > "$TARGET/COMPILAR.bat" <<'BATEOF'
@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
    echo error: Python no esta instalado o no esta en el PATH.
    pause
    exit /b 1
)

python -m pip install --upgrade pip
python -m pip install pyinstaller

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist volume_crypto.spec del /f /q volume_crypto.spec

pyinstaller --onefile --name volume_crypto --console volume_crypto.py

if errorlevel 1 (
    echo error: la compilacion fallo.
    pause
    exit /b 1
)

copy /y "dist\volume_crypto.exe" "volume_crypto.exe" >nul

echo.
echo Compilacion completada.
echo Ejecutable listo: %~dp0volume_crypto.exe
echo.
pause
BATEOF

cat > "$TARGET/requirements-build.txt" <<'REQEOF'
pyinstaller>=6.0
REQEOF

cat > "$TARGET/LEEME.txt" <<'LEEOF'
RUTA:
  /Users/faustosantana/Pruebas

COMPILAR EN WINDOWS SERVER:
  1. Copia esta carpeta al servidor
  2. Ejecuta COMPILAR.bat como administrador
  3. Usa volume_crypto.exe

USO:
  volume_crypto.exe --encrypt C
  volume_crypto.exe --decrypt C --key key.bin
LEEOF

chmod +x "$TARGET/volume_crypto.py"

echo "Listo en: $TARGET"
ls -la "$TARGET"

if command -v open >/dev/null 2>&1; then
  open "$TARGET"
fi
