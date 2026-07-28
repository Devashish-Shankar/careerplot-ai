"""
==========================================================
CareerPilot AI

Shared Package

Repository

Generic repository abstraction.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .identity import Identity
from .pagination import PageRequest, PageResult

T = TypeVar("T")


class Repository(ABC, Generic[T]):
    """
    Generic repository interface.
    """

    @abstractmethod
    def get(self, identity: Identity) -> T:
        """
        Retrieve an entity by identity.

        Raises
        ------
        NotFoundError
            If the entity does not exist.
        """
        raise NotImplementedError

    @abstractmethod
    def get_or_none(self, identity: Identity) -> T | None:
        """
        Retrieve an entity if it exists.
        """
        raise NotImplementedError

    @abstractmethod
    def add(self, entity: T) -> None:
        """
        Add an entity.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: T) -> None:
        """
        Update an entity.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, entity: T) -> None:
        """
        Remove an entity.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(self, identity: Identity) -> bool:
        """
        Check whether an entity exists.
        """
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        """
        Return total entity count.
        """
        raise NotImplementedError

    @abstractmethod
    def list(self) -> tuple[T, ...]:
        """
        Return all entities.
        """
        raise NotImplementedError

    @abstractmethod
    def page(
        self,
        request: PageRequest,
    ) -> PageResult[T]:
        """
        Return paginated entities.
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        """
        Remove all entities.
        """
        raise NotImplementedError
