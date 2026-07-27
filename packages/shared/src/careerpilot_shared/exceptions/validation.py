"""
==========================================================
CareerPilot AI

Shared Package

Validation Exception

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .base import CareerPilotError


class ValidationError(CareerPilotError):
    """
    Raised when user input or request validation fails.
    """

    pass