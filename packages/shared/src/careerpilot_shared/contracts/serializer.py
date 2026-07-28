"""
==========================================================
CareerPilot AI

Shared Package

Serializer Contract

Defines the serialization abstraction used across the
CareerPilot AI platform.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Serializer(ABC, Generic[T]):
    """
    Abstract serializer contract.
    """

    @abstractmethod
    def serialize(self, obj: T) -> bytes:
        """
        Serialize an object into bytes.
        """
        raise NotImplementedError

    @abstractmethod
    def deserialize(self, data: bytes) -> T:
        """
        Deserialize bytes into an object.
        """
        raise NotImplementedError

    @abstractmethod
    def serialize_dict(self, obj: dict[str, Any]) -> bytes:
        """
        Serialize a dictionary into bytes.
        """
        raise NotImplementedError

    @abstractmethod
    def deserialize_dict(
        self,
        data: bytes,
    ) -> dict[str, Any]:
        """
        Deserialize bytes into a dictionary.
        """
        raise NotImplementedError
