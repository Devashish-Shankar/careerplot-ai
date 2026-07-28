"""
==========================================================
CareerPilot AI

Shared Package

File Constants

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from typing import Final

KB: Final[int] = 1024

MB: Final[int] = 1024 * KB

GB: Final[int] = 1024 * MB

MAX_FILE_SIZE: Final[int] = 25 * MB

MAX_RESUME_SIZE: Final[int] = 10 * MB

SUPPORTED_DOCUMENT_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
    }
)

SUPPORTED_IMAGE_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
    }
)
