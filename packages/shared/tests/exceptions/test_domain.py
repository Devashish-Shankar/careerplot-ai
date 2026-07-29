"""
==========================================================
CareerPilot AI

Shared Package Tests

Domain Exception Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from careerpilot_shared.exceptions import CareerPilotError, DomainError


def test_domain_error_is_base_error() -> None:
    error = DomainError(
        message="Domain failure",
        code="DOMAIN_ERROR",
    )

    assert isinstance(error, CareerPilotError)


def test_domain_error_properties() -> None:
    error = DomainError(
        message="Invalid aggregate",
        code="INVALID_AGGREGATE",
    )

    assert error.message == "Invalid aggregate"
    assert error.code == "INVALID_AGGREGATE"
