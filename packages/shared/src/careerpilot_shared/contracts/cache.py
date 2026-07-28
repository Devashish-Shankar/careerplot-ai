"""
==========================================================
CareerPilot AI

Shared Package

Cache Contract

Defines a generic cache abstraction.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from careerpilot_shared.result import Result

T = TypeVar("T")


class Cache(ABC, Generic[T]):
    """
    Generic cache abstraction.
    """

    @abstractmethod
    def get(self, key: str) -> Result[T]:
        raise NotImplementedError

    @abstractmethod
    def set(
        self,
        key: str,
        value: T,
    ) -> Result[None]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: str) -> Result[None]:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> Result[None]:
        raise NotImplementedError