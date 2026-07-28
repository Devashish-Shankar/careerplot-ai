"""
==========================================================
CareerPilot AI

Shared Package

File Size Value Object

Represents an immutable file size.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from careerpilot_shared.exceptions import ValidationError


@dataclass(frozen=True, slots=True)
class FileSize:
    """
    Immutable file size.
    """

    bytes: int

    def __post_init__(self) -> None:
        if self.bytes < 0:
            raise ValidationError(
                message="File size cannot be negative.",
                code="NEGATIVE_FILE_SIZE",
            )

    @classmethod
    def from_bytes(cls, value: int) -> FileSize:
        return cls(value)

    @property
    def kb(self) -> float:
        return self.bytes / 1024

    @property
    def mb(self) -> float:
        return self.bytes / (1024**2)

    @property
    def gb(self) -> float:
        return self.bytes / (1024**3)

    def human_readable(self) -> str:
        if self.bytes < 1024:
            return f"{self.bytes} B"

        if self.bytes < 1024**2:
            return f"{self.kb:.2f} KB"

        if self.bytes < 1024**3:
            return f"{self.mb:.2f} MB"

        return f"{self.gb:.2f} GB"

    def __str__(self) -> str:
        return self.human_readable()
