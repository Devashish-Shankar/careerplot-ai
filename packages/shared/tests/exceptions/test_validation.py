"""
==========================================================
CareerPilot AI

Shared Package Tests

Validation Exception Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import pytest
from careerpilot_shared.exceptions import CareerPilotError, ValidationError


def test_validation_error_is_base_error() -> None:
    error = ValidationError(
        message="Email is invalid.",
        code="INVALID_EMAIL",
    )

    assert isinstance(error, CareerPilotError)


@pytest.mark.parametrize(
    ("message", "code"),
    [
        ("Invalid email", "INVALID_EMAIL"),
        ("Invalid phone", "INVALID_PHONE"),
        ("Invalid URL", "INVALID_URL"),
    ],
)
def test_validation_error_values(
    message: str,
    code: str,
) -> None:
    error = ValidationError(
        message=message,
        code=code,
    )

    assert error.message == message
    assert error.code == code
