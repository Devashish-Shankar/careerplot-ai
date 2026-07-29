"""
==========================================================
CareerPilot AI

Shared Package

Filesystem Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path) -> Path:
    """
    Create a directory if it does not already exist.
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_text(
    path: Path,
    *,
    encoding: str = "utf-8",
) -> str:
    """
    Read text from a file.
    """
    return path.read_text(encoding=encoding)


def write_text(
    path: Path,
    content: str,
    *,
    encoding: str = "utf-8",
) -> None:
    """
    Write text to a file.
    """
    ensure_directory(path.parent)
    path.write_text(content, encoding=encoding)


def read_bytes(path: Path) -> bytes:
    """
    Read bytes from a file.
    """
    return path.read_bytes()


def write_bytes(
    path: Path,
    content: bytes,
) -> None:
    """
    Write bytes to a file.
    """
    ensure_directory(path.parent)
    path.write_bytes(content)


def delete_file(path: Path) -> bool:
    """
    Delete a file if it exists.
    """
    if not path.exists():
        return False

    path.unlink()
    return True


def file_exists(path: Path) -> bool:
    """
    Return True if the path exists and is a file.
    """
    return path.is_file()


def directory_exists(path: Path) -> bool:
    """
    Return True if the path exists and is a directory.
    """
    return path.is_dir()


def file_size(path: Path) -> int:
    """
    Return the file size in bytes.
    """
    return path.stat().st_size


def list_files(
    directory: Path,
    *,
    recursive: bool = False,
) -> list[Path]:
    """
    List files inside a directory.
    """
    if recursive:
        return [path for path in directory.rglob("*") if path.is_file()]

    return [path for path in directory.iterdir() if path.is_file()]
