"""
==========================================================
CareerPilot AI

Shared Package

Pagination

Provides pagination request and response models.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import ceil
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class PageRequest:
    """
    Represents a pagination request.
    """

    page: int = 1
    page_size: int = 20

    def __post_init__(self) -> None:
        if self.page < 1:
            raise ValueError("Page number must be greater than zero.")

        if self.page_size < 1:
            raise ValueError("Page size must be greater than zero.")


@dataclass(frozen=True, slots=True)
class PageResult(Generic[T]):
    """
    Represents a paginated result.
    """

    items: tuple[T, ...] = field(default_factory=tuple)
    total: int = 0
    page: int = 1
    page_size: int = 20

    @property
    def total_pages(self) -> int:
        if self.total == 0:
            return 0
        return ceil(self.total / self.page_size)

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages

    @property
    def has_previous(self) -> bool:
        return self.page > 1
