"""
==========================================================
CareerPilot AI

Shared Package

Domain Event

Represents immutable business events.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from .identity import Identity


@dataclass(frozen=True, slots=True)
class DomainEvent:
    """
    Base class for domain events.
    """

    aggregate_id: Identity

    payload: dict[str, Any] = field(default_factory=lambda: {})

    event_id: Identity = field(default_factory=Identity.generate)

    occurred_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    event_version: int = 1

    @property
    def event_name(self) -> str:
        return self.__class__.__name__

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": str(self.event_id),
            "aggregate_id": str(self.aggregate_id),
            "event_name": self.event_name,
            "event_version": self.event_version,
            "occurred_at": self.occurred_at.isoformat(),
            "payload": self.payload,
        }
