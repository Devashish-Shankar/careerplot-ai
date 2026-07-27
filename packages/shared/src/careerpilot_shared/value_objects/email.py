"""
==========================================================
CareerPilot AI

Shared Package

Email Value Object

Represents an immutable email address.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from careerpilot_shared.exceptions import ValidationError

_EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)


@dataclass(frozen=True, slots=True)
class Email:
    """
    Immutable email value object.
    """

    value: str

    def __post_init__(self) -> None:
        email = self.value.strip().lower()

        if not _EMAIL_PATTERN.fullmatch(email):
            raise ValidationError(
                message="Invalid email address.",
                code="INVALID_EMAIL",
            )

        object.__setattr__(self, "value", email)

    @property
    def username(self) -> str:
        return self.value.split("@")[0]

    @property
    def domain(self) -> str:
        return self.value.split("@")[1]

    def __str__(self) -> str:
        return self.value