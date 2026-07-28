"""
==========================================================
CareerPilot AI

Shared Package

Resume Constants

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from typing import Final

DEFAULT_RESUME_LANGUAGE: Final[str] = "en"

MAX_RESUME_PAGES: Final[int] = 10

MIN_RESUME_TEXT_LENGTH: Final[int] = 100

SUPPORTED_RESUME_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".pdf",
        ".doc",
        ".docx",
    }
)
