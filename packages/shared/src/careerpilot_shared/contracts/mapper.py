"""
==========================================================
CareerPilot AI

Shared Package

Mapper Contract

Defines the object mapping abstraction.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

S = TypeVar("S")
T = TypeVar("T")


class Mapper(ABC, Generic[S, T]):
    """
    Generic object mapper.
    """

    @abstractmethod
    def map(self, source: S) -> T:
        """
        Map one object into another.
        """
        raise NotImplementedError