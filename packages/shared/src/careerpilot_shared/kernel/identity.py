"""
==========================================================
CareerPilot AI

Shared Package

Identity

Provides a stable abstraction over UniqueId.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from careerpilot_shared.value_objects import UniqueId


@dataclass(frozen=True, slots=True)
class Identity:
    """
    Represents the identity of an entity.
    """

    value: UniqueId

    @classmethod
    def generate(cls) -> Identity:
        return cls(UniqueId.generate())

    @classmethod
    def from_string(cls, value: str) -> Identity:
        return cls(UniqueId.from_string(value))

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Identity({self.value})"
