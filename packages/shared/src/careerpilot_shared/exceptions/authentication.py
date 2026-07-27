"""
==========================================================
CareerPilot AI

Shared Package

Authentication Exception

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .base import CareerPilotError


class AuthenticationError(CareerPilotError):
    """
    Raised when user authentication fails.
    """

    pass