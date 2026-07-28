"""
==========================================================
CareerPilot AI

Shared Package

Unique Identifier Value Object

Provides an immutable UUID-based identifier that is used
throughout the platform.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class UniqueId:
    """
    Immutable UUID value object.
    """

    value: UUID

    @classmethod
    def generate(cls) -> UniqueId:
        """
        Generate a new unique identifier.
        """
        return cls(uuid4())

    @classmethod
    def from_string(cls, value: str) -> UniqueId:
        """
        Create a UniqueId from a UUID string.

        Raises
        ------
        ValueError
            If the UUID string is invalid.
        """
        return cls(UUID(value))

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"UniqueId('{self.value}')"
