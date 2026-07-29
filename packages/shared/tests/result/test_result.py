"""
==========================================================
CareerPilot AI

Shared Package Tests

Result Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from careerpilot_shared.result import Failure, Result, Success


def test_success_result() -> None:
    result = Success(100)

    assert isinstance(result, Result)
    assert result.is_success
    assert not result.is_failure
    assert result.value == 100
    assert result.error is None


def test_failure_result() -> None:
    error = ValueError("Something went wrong.")

    result = Failure(error)

    assert isinstance(result, Result)
    assert result.is_failure
    assert not result.is_success
    assert result.error is error
