"""
==========================================================
CareerPilot AI

Shared Package

Regex Constants

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from typing import Final

EMAIL_REGEX: Final[str] = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

PHONE_REGEX: Final[str] = r"^\+?[1-9]\d{7,14}$"

URL_REGEX: Final[str] = r"^https?://.+"

LINKEDIN_REGEX: Final[str] = r"^https?://(www\.)?linkedin\.com/.*$"

GITHUB_REGEX: Final[str] = r"^https?://(www\.)?github\.com/.*$"
