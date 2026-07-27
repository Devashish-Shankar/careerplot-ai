"""
==========================================================
CareerPilot AI

Shared Package

Not Found Exception

Raised when a requested resource cannot be located.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .base import CareerPilotError


class NotFoundError(CareerPilotError):
    """
    Raised when a requested resource does not exist.

    Examples
    --------
    - Resume not found
    - Candidate not found
    - Job not found
    """

    pass