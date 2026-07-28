"""
==========================================================
CareerPilot AI

Shared Package

Logger Contract

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Logger(ABC):
    """
    Generic logger abstraction.
    """

    @abstractmethod
    def debug(self, message: str, **context: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def info(self, message: str, **context: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def warning(self, message: str, **context: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def error(self, message: str, **context: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def critical(self, message: str, **context: Any) -> None:
        raise NotImplementedError