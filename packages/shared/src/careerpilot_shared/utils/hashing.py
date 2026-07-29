"""
==========================================================
CareerPilot AI

Shared Package

Hashing Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import hashlib


def sha256(value: str) -> str:
    """
    Compute SHA-256 hash.
    """
    return hashlib.sha256(
        value.encode("utf-8"),
    ).hexdigest()


def sha512(value: str) -> str:
    """
    Compute SHA-512 hash.
    """
    return hashlib.sha512(
        value.encode("utf-8"),
    ).hexdigest()


def md5(value: str) -> str:
    """
    Compute MD5 hash.

    Notes
    -----
    Intended only for non-security use cases.
    """
    return hashlib.md5(  # noqa: S324
        value.encode("utf-8"),
    ).hexdigest()


def file_sha256(data: bytes) -> str:
    """
    Compute SHA-256 hash of bytes.
    """
    return hashlib.sha256(data).hexdigest()


def file_sha512(data: bytes) -> str:
    """
    Compute SHA-512 hash of bytes.
    """
    return hashlib.sha512(data).hexdigest()


def verify_sha256(
    value: str,
    expected_hash: str,
) -> bool:
    """
    Verify SHA-256 hash.
    """
    return sha256(value) == expected_hash
