"""
==========================================================
CareerPilot AI

Shared Package

Unit Of Work

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Self


class UnitOfWork(ABC):
    """
    Base Unit of Work.
    """

    @abstractmethod
    def begin(self) -> None:
        """
        Begin a transaction.
        """
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        """
        Commit the transaction.
        """
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        """
        Rollback the transaction.
        """
        raise NotImplementedError

    @abstractmethod
    def flush(self) -> None:
        """
        Flush pending changes.
        """
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        """
        Close the unit of work.
        """
        raise NotImplementedError

    def __enter__(self) -> Self:
        self.begin()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: object | None,
    ) -> bool:
        if exc is None:
            self.commit()
        else:
            self.rollback()

        self.close()
        return False
