"""
==========================================================
CareerPilot AI

Shared Package

Result Pattern

Provides a strongly typed Result abstraction for handling
successful and failed operations without relying on exceptions
for normal application flow.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Result(Generic[T]):
    """
    Represents the outcome of an operation.

    A Result contains either:

    - a successful value
    - or an exception

    Never both.
    """

    value: T | None = None
    error: Exception | None = None

    def __post_init__(self) -> None:
        """
        Validate that the Result is in a consistent state.

        Exactly one of `value` or `error` must be present.
        """

        has_value = self.value is not None
        has_error = self.error is not None

        if has_value == has_error:
            raise ValueError(
                "Result must contain either a value or an error, but not both."
            )

    @property
    def is_success(self) -> bool:
        """Return True if the operation completed successfully."""
        return self.error is None

    @property
    def is_failure(self) -> bool:
        """Return True if the operation failed."""
        return self.error is not None