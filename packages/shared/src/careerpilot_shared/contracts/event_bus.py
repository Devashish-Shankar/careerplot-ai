"""
==========================================================
CareerPilot AI

Shared Package

Event Bus Contract

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from careerpilot_shared.kernel import DomainEvent
from careerpilot_shared.result import Result


class EventBus(ABC):
    """
    Domain event publisher.
    """

    @abstractmethod
    def publish(
        self,
        event: DomainEvent,
    ) -> Result[None]:
        """
        Publish a single domain event.
        """
        raise NotImplementedError

    @abstractmethod
    def publish_many(
        self,
        events: tuple[DomainEvent, ...],
    ) -> Result[None]:
        """
        Publish multiple domain events.
        """
        raise NotImplementedError