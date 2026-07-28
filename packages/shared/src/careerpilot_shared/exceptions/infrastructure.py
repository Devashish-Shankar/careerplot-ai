"""
==========================================================
CareerPilot AI

Shared Package

Infrastructure Exception

Represents failures originating from external systems.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .base import CareerPilotError


class InfrastructureError(CareerPilotError):
    """
    Raised when an infrastructure component fails.

    Examples
    --------
    - Database unavailable
    - Redis unavailable
    - S3 upload failure
    - LLM timeout
    """

    pass
