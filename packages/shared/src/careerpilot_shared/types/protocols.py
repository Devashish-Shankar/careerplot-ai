"""
==========================================================
CareerPilot AI

Shared Package

Typing Protocols

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class SupportsToDict(Protocol):
    """
    Represents an object that can be converted
    into a dictionary.
    """

    def to_dict(self) -> dict[str, Any]: ...


@runtime_checkable
class SupportsFromDict(Protocol):
    """
    Represents an object that can be created
    from a dictionary.
    """

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> SupportsFromDict: ...
