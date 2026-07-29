"""
==========================================================
CareerPilot AI

Shared Package

Random Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import secrets
import string

_ALPHABET = string.ascii_letters + string.digits


def random_string(length: int = 16) -> str:
    """
    Generate a secure random string.
    """
    if length < 1:
        raise ValueError("Length must be greater than zero.")

    return "".join(secrets.choice(_ALPHABET) for _ in range(length))


def random_digits(length: int = 6) -> str:
    """
    Generate random numeric digits.
    """
    if length < 1:
        raise ValueError("Length must be greater than zero.")

    return "".join(secrets.choice(string.digits) for _ in range(length))


def random_hex(length: int = 32) -> str:
    """
    Generate a hexadecimal token.
    """
    if length < 1:
        raise ValueError("Length must be greater than zero.")

    return secrets.token_hex((length + 1) // 2)[:length]


def random_urlsafe(length: int = 32) -> str:
    """
    Generate a URL-safe random token.
    """
    if length < 1:
        raise ValueError("Length must be greater than zero.")

    token = secrets.token_urlsafe(length)

    return token[:length]
