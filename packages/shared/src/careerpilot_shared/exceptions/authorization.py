"""
==========================================================
CareerPilot AI

Shared Package

Authorization Exception

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .base import CareerPilotError


class AuthorizationError(CareerPilotError):
    """
    Raised when a user lacks permission to perform
    an operation.
    """

    pass