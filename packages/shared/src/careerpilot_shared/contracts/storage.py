"""
==========================================================
CareerPilot AI

Shared Package

Storage Contract

Defines a generic storage abstraction.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from careerpilot_shared.result import Result


class Storage(ABC):
    """
    Generic storage abstraction.
    """

    @abstractmethod
    def exists(self, path: str) -> bool:
        """
        Determine whether a resource exists.
        """
        raise NotImplementedError

    @abstractmethod
    def save(
        self,
        source: Path,
        destination: str,
    ) -> Result[str]:
        """
        Save a file.

        Returns
        -------
        Result[str]
            Storage location.
        """
        raise NotImplementedError

    @abstractmethod
    def read(self, path: str) -> Result[bytes]:
        """
        Read bytes from storage.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, path: str) -> Result[None]:
        """
        Delete a stored resource.
        """
        raise NotImplementedError
