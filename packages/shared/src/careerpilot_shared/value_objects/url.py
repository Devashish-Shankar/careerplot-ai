"""
==========================================================
CareerPilot AI

Shared Package

URL Value Object

Represents an immutable HTTP/HTTPS URL.

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlparse

from careerpilot_shared.exceptions import ValidationError


@dataclass(frozen=True, slots=True)
class Url:
    """
    Immutable URL value object.
    """

    value: str

    def __post_init__(self) -> None:
        parsed = urlparse(self.value)

        if parsed.scheme not in {"http", "https"}:
            raise ValidationError(
                message="Only HTTP and HTTPS URLs are supported.",
                code="INVALID_URL_SCHEME",
            )

        if not parsed.netloc:
            raise ValidationError(
                message="Invalid URL.",
                code="INVALID_URL",
            )

    @property
    def scheme(self) -> str:
        return urlparse(self.value).scheme

    @property
    def host(self) -> str:
        return urlparse(self.value).netloc

    @property
    def path(self) -> str:
        return urlparse(self.value).path

    def __str__(self) -> str:
        return self.value
