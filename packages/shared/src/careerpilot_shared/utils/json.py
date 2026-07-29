"""
==========================================================
CareerPilot AI

Shared Package

JSON Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import json
from typing import cast

from careerpilot_shared.types import JsonObject


def load_json(value: str) -> JsonObject:
    """
    Deserialize a JSON string into a JsonObject.

    Raises
    ------
    TypeError
        If the root JSON value is not an object.
    """
    data = json.loads(value)

    if not isinstance(data, dict):
        raise TypeError("Expected a JSON object.")

    return cast(JsonObject, data)


def dump_json(
    value: JsonObject,
    *,
    indent: int | None = None,
    sort_keys: bool = False,
) -> str:
    """
    Serialize a JsonObject into a JSON string.
    """
    return json.dumps(
        value,
        indent=indent,
        sort_keys=sort_keys,
        ensure_ascii=False,
    )


def pretty_json(value: JsonObject) -> str:
    """
    Return a human-readable JSON string.
    """
    return dump_json(
        value,
        indent=4,
        sort_keys=True,
    )


def minify_json(value: JsonObject) -> str:
    """
    Return a compact JSON string.
    """
    return json.dumps(
        value,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def is_valid_json(value: str) -> bool:
    """
    Return True if the supplied string is valid JSON.
    """
    try:
        json.loads(value)
    except json.JSONDecodeError:
        return False

    return True
