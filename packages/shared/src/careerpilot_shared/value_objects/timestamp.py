"""
==========================================================
CareerPilot AI

Shared Package

Timestamp Value Object

Provides an immutable UTC timestamp.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class Timestamp:
    """
    Immutable UTC timestamp.
    """

    value: datetime

    @classmethod
    def now(cls) -> Timestamp:
        """
        Create a timestamp using the current UTC time.
        """
        return cls(datetime.now(UTC))

    @classmethod
    def from_datetime(cls, value: datetime) -> Timestamp:
        """
        Create a Timestamp from an existing datetime.
        """
        if value.tzinfo is None:
            value = value.replace(tzinfo=UTC)

        return cls(value.astimezone(UTC))

    def isoformat(self) -> str:
        """
        Return ISO-8601 representation.
        """
        return self.value.isoformat()

    def __str__(self) -> str:
        return self.isoformat()
