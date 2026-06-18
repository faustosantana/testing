#!/usr/bin/env python3

import argparse
import os
import platform
import secrets
import subprocess
import sys

KEY_FILE = "key.bin"
KEY_SIZE = 32


class VolumeCryptoError(Exception):
    pass


def generate_key() -> bytes:
    return secrets.token_bytes(KEY_SIZE)


def save_key(key: bytes, path: str) -> None:
    with open(path, "wb") as handle:
        handle.write(key)


def load_key(path: str) -> bytes:
    with open(path, "rb") as handle:
        return handle.read()


def run_command(command: list[str]) -> None:
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise VolumeCryptoError(detail or f"command failed: {' '.join(command)}")


def mapper_name(target: str) -> str:
    base = os.path.basename(target.rstrip(os.sep))
    sanitized = "".join(ch if ch.isalnum() else "_" for ch in base)
    return sanitized or "volume"


def encrypt_linux(target: str, key_path: str) -> None:
    run_command(
        [
            "cryptsetup",
            "luksFormat",
            "--batch-mode",
            "--type",
            "luks2",
            "--key-file",
            key_path,
            "--key-size",
            str(KEY_SIZE * 8),
            target,
        ]
    )


def decrypt_linux(target: str, key_path: str) -> None:
    run_command(
        [
            "cryptsetup",
            "open",
            "--key-file",
            key_path,
            target,
            mapper_name(target),
        ]
    )


def encrypt_windows(target: str, key_path: str) -> None:
    run_command(
        [
            "manage-bde",
            "-on",
            target,
            "-used",
        ]
    )
    run_command(
        [
            "manage-bde",
            "-protectors",
            "-add",
            target,
            "-ExternalKey",
            key_path,
        ]
    )


def decrypt_windows(target: str, key_path: str) -> None:
    run_command(
        [
            "manage-bde",
            "-unlock",
            target,
            "-ExternalKey",
            key_path,
        ]
    )


def encrypt_volume(target: str, key_path: str) -> None:
    if platform.system() == "Windows":
        encrypt_windows(target, key_path)
    else:
        encrypt_linux(target, key_path)


def decrypt_volume(target: str, key_path: str) -> None:
    if platform.system() == "Windows":
        decrypt_windows(target, key_path)
    else:
        decrypt_linux(target, key_path)


def handle_encrypt(target: str) -> int:
    key_path = os.path.abspath(KEY_FILE)
    if os.path.exists(key_path):
        print(f"error: {key_path} already exists", file=sys.stderr)
        return 1

    key = generate_key()
    save_key(key, key_path)

    try:
        encrypt_volume(target, key_path)
    except VolumeCryptoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print("success: volume encrypted")
    print(f"key: {key_path}")
    return 0


def handle_decrypt(target: str, key_path: str) -> int:
    resolved_key = os.path.abspath(key_path)
    if not os.path.isfile(resolved_key):
        print(f"error: key file not found: {resolved_key}", file=sys.stderr)
        return 1

    try:
        decrypt_volume(target, resolved_key)
    except VolumeCryptoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print("success: volume decrypted")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt", metavar="target")
    group.add_argument("--decrypt", metavar="target")
    parser.add_argument("--key", metavar="file")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.encrypt is not None:
        return handle_encrypt(args.encrypt)

    if not args.key:
        print("error: --key is required for decryption", file=sys.stderr)
        return 1

    return handle_decrypt(args.decrypt, args.key)


if __name__ == "__main__":
    sys.exit(main())
