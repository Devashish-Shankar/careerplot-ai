"""
==========================================================
CareerPilot AI

Shared Package Tests

Base Exception Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import pytest
from careerpilot_shared.exceptions import CareerPilotError


def test_create_base_exception() -> None:
    error = CareerPilotError(
        message="Something went wrong.",
        code="TEST_ERROR",
    )

    assert error.message == "Something went wrong."
    assert error.code == "TEST_ERROR"
    assert error.details is None
    assert error.cause is None


def test_string_representation() -> None:
    error = CareerPilotError(
        message="Failure",
        code="FAILURE",
    )

    assert str(error) == "[FAILURE] Failure"


@pytest.mark.parametrize(
    ("message", "code"),
    [
        ("Error 1", "ERR1"),
        ("Error 2", "ERR2"),
        ("Database Error", "DB001"),
    ],
)
def test_multiple_errors(
    message: str,
    code: str,
) -> None:
    error = CareerPilotError(
        message=message,
        code=code,
    )

    assert error.message == message
    assert error.code == code
