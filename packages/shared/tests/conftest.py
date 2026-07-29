"""
==========================================================
CareerPilot AI

Shared Package Tests

Pytest Configuration

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import pytest


@pytest.fixture
def sample_message() -> str:
    """
    Sample message fixture used across tests.
    """
    return "Something went wrong."


@pytest.fixture
def sample_code() -> str:
    """
    Sample error code fixture.
    """
    return "TEST_ERROR"


@pytest.fixture
def sample_details() -> dict[str, object]:
    """
    Sample details fixture.
    """
    return {
        "field": "email",
        "reason": "invalid",
    }
