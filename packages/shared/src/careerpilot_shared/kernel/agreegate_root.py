"""
==========================================================
CareerPilot AI

Shared Package

Aggregate Root

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .domain_event import DomainEvent
from .entity import Entity


@dataclass(eq=False, slots=True)
class AggregateRoot(Entity):
    """
    Base class for aggregate roots.

    Aggregate roots own domain events.
    """

    _domain_events: list[DomainEvent] = field(
        default_factory=lambda: [],
        init=False,
        repr=False,
    )

    @property
    def domain_events(self) -> tuple[DomainEvent, ...]:
        """
        Immutable view of pending events.
        """
        return tuple(self._domain_events)

    @property
    def has_domain_events(self) -> bool:
        return bool(self._domain_events)

    def add_domain_event(self, event: DomainEvent) -> None:
        """
        Register a domain event.
        """
        self._domain_events.append(event)

    def pull_domain_events(self) -> tuple[DomainEvent, ...]:
        """
        Return all pending events and clear them.
        """
        events = tuple(self._domain_events)
        self._domain_events.clear()
        return events

    def clear_domain_events(self) -> None:
        """
        Remove all pending domain events.
        """
        self._domain_events.clear()
