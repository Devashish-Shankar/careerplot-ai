"""
==========================================================
CareerPilot AI

Shared Package

Specification

Provides the Specification pattern for composing
business rules.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Specification(ABC, Generic[T]):
    """
    Base Specification.
    """

    @abstractmethod
    def is_satisfied_by(self, candidate: T) -> bool:
        """
        Determine whether the candidate satisfies
        this specification.
        """
        raise NotImplementedError

    def __call__(self, candidate: T) -> bool:
        return self.is_satisfied_by(candidate)

    def and_(self, other: Specification[T]) -> Specification[T]:
        return AndSpecification(self, other)

    def or_(self, other: Specification[T]) -> Specification[T]:
        return OrSpecification(self, other)

    def not_(self) -> Specification[T]:
        return NotSpecification(self)


class AndSpecification(Specification[T]):
    """
    Logical AND specification.
    """

    def __init__(
        self,
        left: Specification[T],
        right: Specification[T],
    ) -> None:
        self._left = left
        self._right = right

    def is_satisfied_by(self, candidate: T) -> bool:
        return self._left.is_satisfied_by(candidate) and self._right.is_satisfied_by(candidate)


class OrSpecification(Specification[T]):
    """
    Logical OR specification.
    """

    def __init__(
        self,
        left: Specification[T],
        right: Specification[T],
    ) -> None:
        self._left = left
        self._right = right

    def is_satisfied_by(self, candidate: T) -> bool:
        return self._left.is_satisfied_by(candidate) or self._right.is_satisfied_by(candidate)


class NotSpecification(Specification[T]):
    """
    Logical NOT specification.
    """

    def __init__(
        self,
        specification: Specification[T],
    ) -> None:
        self._specification = specification

    def is_satisfied_by(self, candidate: T) -> bool:
        return not self._specification.is_satisfied_by(candidate)
