"""
==========================================================
CareerPilot AI

Shared Package

Parser Contract

Defines a generic parser abstraction.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generic, TypeVar

T = TypeVar("T")


class Parser(ABC, Generic[T]):
    """
    Generic parser contract.
    """

    @abstractmethod
    def parse(self, source: Path) -> T:
        """
        Parse a source file into an object.
        """
        raise NotImplementedError

    @abstractmethod
    def supports(self, source: Path) -> bool:
        """
        Determine whether this parser supports
        the given source.
        """
        raise NotImplementedError
