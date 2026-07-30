"""
==========================================================
CareerPilot AI

Shared Package Tests

Clock Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from datetime import UTC, datetime

from careerpilot_shared.kernel import SystemClock


def test_now_returns_datetime() -> None:
    now = SystemClock().now()

    assert isinstance(now, datetime)


def test_now_is_timezone_aware() -> None:
    now = SystemClock().now()

    assert now.tzinfo == UTC


def test_multiple_calls_return_datetime() -> None:
    first = SystemClock().now()
    second = SystemClock().now()

    assert isinstance(first, datetime)
    assert isinstance(second, datetime)