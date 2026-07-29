"""
==========================================================
CareerPilot AI

Shared Package Tests

Infrastructure Exception Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from careerpilot_shared.exceptions import CareerPilotError, InfrastructureError


def test_infrastructure_error_is_base_error() -> None:
    error = InfrastructureError(
        message="Database unavailable",
        code="DATABASE_ERROR",
    )

    assert isinstance(error, CareerPilotError)


def test_infrastructure_error_properties() -> None:
    error = InfrastructureError(
        message="Redis unavailable",
        code="CACHE_ERROR",
    )

    assert error.message == "Redis unavailable"
    assert error.code == "CACHE_ERROR"
