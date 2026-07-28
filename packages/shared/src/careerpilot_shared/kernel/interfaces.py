"""
==========================================================
CareerPilot AI

Shared Package

Interfaces

Shared protocol definitions used across
the CareerPilot AI platform.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Protocol, runtime_checkable

from .identity import Identity


@runtime_checkable
class HasIdentity(Protocol):
    """
    Represents an object that exposes an identity.
    """

    @property
    def id(self) -> Identity: ...


@runtime_checkable
class HasTimestamp(Protocol):
    """
    Represents an object that exposes
    creation and update timestamps.
    """

    @property
    def created_at(self) -> datetime: ...

    @property
    def updated_at(self) -> datetime: ...


@runtime_checkable
class Serializable(Protocol):
    """
    Represents an object that can be serialized.
    """

    def to_dict(self) -> dict[str, Any]: ...


@runtime_checkable
class Auditable(Protocol):
    """
    Represents an auditable object.
    """

    @property
    def created_by(self) -> Identity: ...

    @property
    def updated_by(self) -> Identity: ...
