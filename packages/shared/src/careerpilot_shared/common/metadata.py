"""
==========================================================
CareerPilot AI

Shared Package

Metadata

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import cast

from careerpilot_shared.types import JsonObject, JsonValue


@dataclass(slots=True)
class Metadata:
    """
    Generic metadata container.

    Stores JSON-serializable metadata as key/value pairs.
    """

    values: JsonObject = field(
        default_factory=lambda: cast(JsonObject, {}),
    )

    def get(
        self,
        key: str,
        default: JsonValue | None = None,
    ) -> JsonValue | None:
        """
        Retrieve a metadata value.
        """
        return self.values.get(key, default)

    def set(
        self,
        key: str,
        value: JsonValue,
    ) -> None:
        """
        Set a metadata value.
        """
        self.values[key] = value

    def update(
        self,
        values: JsonObject,
    ) -> None:
        """
        Merge metadata values.
        """
        self.values.update(values)

    def remove(
        self,
        key: str,
    ) -> JsonValue | None:
        """
        Remove a metadata entry.
        """
        return self.values.pop(key, None)

    def contains(
        self,
        key: str,
    ) -> bool:
        """
        Check whether a metadata key exists.
        """
        return key in self.values

    def clear(self) -> None:
        """
        Remove all metadata.
        """
        self.values.clear()

    def to_dict(self) -> JsonObject:
        """
        Return a shallow copy of the metadata.
        """
        return dict(self.values)
