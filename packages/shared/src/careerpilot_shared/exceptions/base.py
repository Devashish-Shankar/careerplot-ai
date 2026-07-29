"""
==========================================================
CareerPilot AI

Shared Package

Base Exception

Defines the root exception for the entire CareerPilot AI
platform.

Every custom exception in the project must inherit from
CareerPilotError.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CareerPilotError(Exception):
    """
    Base exception for the CareerPilot AI platform.
    """

    message: str
    code: str
    details: dict[str, Any] | None = field(default=None)
    cause: Exception | None = field(default=None)

    def __post_init__(self) -> None:
        Exception.__init__(self, self.message)

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"