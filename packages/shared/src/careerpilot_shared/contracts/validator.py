"""
==========================================================
CareerPilot AI

Shared Package

Validator Contract

Defines the validation abstraction.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Validator(ABC, Generic[T]):
    """
    Generic validator contract.
    """

    @abstractmethod
    def validate(self, value: T) -> None:
        """
        Validate the supplied value.

        Raises
        ------
        ValidationError
            If validation fails.
        """
        raise NotImplementedError

    def __call__(self, value: T) -> None:
        """
        Allow validator instances to be called
        like functions.
        """
        self.validate(value)