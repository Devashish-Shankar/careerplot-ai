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


@dataclass(slots=True)
class CareerPilotError(Exception):
    """
    Base exception for the CareerPilot AI platform.

    Parameters
    ----------
    message:
        Human-readable error message.

    code:
        Machine-readable error code.

    details:
        Optional structured metadata.

    cause:
        Original exception that caused this error.
    """

    message: str
    code: str
    details: dict[str, Any] | None = field(default=None)
    cause: Exception | None = field(default=None)

    def __post_init__(self) -> None:
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"