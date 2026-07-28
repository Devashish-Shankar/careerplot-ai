"""
==========================================================
CareerPilot AI

Shared Package

API Constants

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from typing import Final

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRIES: Final[int] = 3

DEFAULT_BACKOFF_SECONDS: Final[int] = 2

DEFAULT_USER_AGENT: Final[str] = "CareerPilot-AI/1.0"

DEFAULT_PAGE_SIZE: Final[int] = 20

MAX_PAGE_SIZE: Final[int] = 100
