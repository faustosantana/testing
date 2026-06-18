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
