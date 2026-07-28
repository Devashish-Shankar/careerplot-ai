"""
==========================================================
CareerPilot AI

Shared Package

Domain Exception

Represents business rule violations.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .base import CareerPilotError


class DomainError(CareerPilotError):
    """
    Raised when a domain rule is violated.

    Examples
    --------
    - Resume exceeds allowed page count.
    - Candidate profile is incomplete.
    - Application already submitted.
    """

    pass
