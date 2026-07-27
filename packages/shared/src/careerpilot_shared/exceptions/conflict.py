"""
==========================================================
CareerPilot AI

Shared Package

Conflict Exception

Raised when a requested operation cannot be completed
because the current resource state conflicts with the
requested action.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .base import CareerPilotError


class ConflictError(CareerPilotError):
    """
    Raised when a resource conflict occurs.

    Examples
    --------
    - User already exists
    - Resume version already exists
    - Job already bookmarked
    """

    pass