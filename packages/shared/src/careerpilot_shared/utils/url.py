"""
==========================================================
CareerPilot AI

Shared Package

URL Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


def join_url(base: str, path: str) -> str:
    """
    Join a base URL with a path.
    """
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


def strip_query(url: str) -> str:
    """
    Remove query parameters from a URL.
    """
    parsed = urlparse(url)

    return urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            "",
            "",
            "",
        )
    )


def query_params(url: str) -> dict[str, list[str]]:
    """
    Return URL query parameters.
    """
    return parse_qs(urlparse(url).query)


def add_query_params(
    url: str,
    params: dict[str, str],
) -> str:
    """
    Add query parameters to a URL.
    """
    parsed = urlparse(url)

    current = parse_qs(parsed.query)

    for key, value in params.items():
        current[key] = [value]

    return urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            urlencode(current, doseq=True),
            parsed.fragment,
        )
    )


def is_secure_url(url: str) -> bool:
    """
    Return True if the URL uses HTTPS.
    """
    return urlparse(url).scheme.lower() == "https"
