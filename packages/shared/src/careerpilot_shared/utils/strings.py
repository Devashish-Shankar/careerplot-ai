"""
==========================================================
CareerPilot AI

Shared Package

String Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import re
import unicodedata


def is_blank(value: str) -> bool:
    """
    Return True if the string contains only whitespace.
    """
    return not value.strip()


def normalize(value: str) -> str:
    """
    Normalize Unicode text.
    """
    return unicodedata.normalize("NFKC", value).strip()


def remove_whitespace(value: str) -> str:
    """
    Remove all whitespace characters.
    """
    return "".join(value.split())


def snake_case(value: str) -> str:
    """
    Convert text to snake_case.
    """
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[\s\-]+", "_", value)
    return value.lower()


def camel_case(value: str) -> str:
    """
    Convert text to camelCase.
    """
    words = snake_case(value).split("_")
    if not words:
        return ""

    return words[0] + "".join(word.capitalize() for word in words[1:])


def pascal_case(value: str) -> str:
    """
    Convert text to PascalCase.
    """
    return "".join(word.capitalize() for word in snake_case(value).split("_"))


def kebab_case(value: str) -> str:
    """
    Convert text to kebab-case.
    """
    return snake_case(value).replace("_", "-")


def slugify(value: str) -> str:
    """
    Create a URL-friendly slug.
    """
    value = normalize(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def truncate(
    value: str,
    length: int,
    suffix: str = "...",
) -> str:
    """
    Truncate a string.
    """
    if len(value) <= length:
        return value

    return value[: length - len(suffix)] + suffix


def starts_with_ignore_case(
    value: str,
    prefix: str,
) -> bool:
    return value.lower().startswith(prefix.lower())


def ends_with_ignore_case(
    value: str,
    suffix: str,
) -> bool:
    return value.lower().endswith(suffix.lower())


def equals_ignore_case(
    left: str,
    right: str,
) -> bool:
    return left.casefold() == right.casefold()
