"""
==========================================================
CareerPilot AI

Shared Package

Clock

Provides a time abstraction for the domain layer.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import UTC, date, datetime


class Clock(ABC):
    """
    Abstract clock interface.

    Prevents direct usage of datetime.now()
    inside the domain layer.
    """

    @abstractmethod
    def now(self) -> datetime:
        """
        Return the current UTC datetime.
        """
        raise NotImplementedError

    @abstractmethod
    def today(self) -> date:
        """
        Return today's UTC date.
        """
        raise NotImplementedError


class SystemClock(Clock):
    """
    System clock implementation.
    """

    def now(self) -> datetime:
        return datetime.now(UTC)

    def today(self) -> date:
        return self.now().date()
