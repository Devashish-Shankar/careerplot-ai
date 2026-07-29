"""
==========================================================
CareerPilot AI

Shared Package

Mixins

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class TimestampMixin:
    """
    Adds creation and update timestamps.
    """

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def touch(self) -> None:
        """
        Update the modification timestamp.
        """
        self.updated_at = datetime.now(UTC)


@dataclass(slots=True)
class SoftDeleteMixin:
    """
    Adds soft-delete capability.
    """

    deleted_at: datetime | None = None

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None

    def delete(self) -> None:
        self.deleted_at = datetime.now(UTC)

    def restore(self) -> None:
        self.deleted_at = None
