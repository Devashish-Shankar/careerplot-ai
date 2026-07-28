"""
==========================================================
CareerPilot AI

Shared Package

Entity

Base class for all domain entities.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .identity import Identity


@dataclass(eq=False, slots=True)
class Entity:
    """
    Base class for all entities.

    Equality is based only on identity.
    """

    id: Identity = field(default_factory=Identity.generate)

    @property
    def identity(self) -> Identity:
        return self.id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False

        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id})"
