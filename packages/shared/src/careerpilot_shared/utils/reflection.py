"""
==========================================================
CareerPilot AI

Shared Package

Reflection Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from typing import Any


def class_name(obj: object) -> str:
    """
    Return the class name of an object.
    """
    return obj.__class__.__name__


def module_name(obj: object) -> str:
    """
    Return the module name of an object.
    """
    return obj.__class__.__module__


def qualified_name(obj: object) -> str:
    """
    Return the fully qualified class name.
    """
    return f"{module_name(obj)}.{class_name(obj)}"


def has_attribute(
    obj: object,
    attribute: str,
) -> bool:
    """
    Check whether an object has an attribute.
    """
    return hasattr(obj, attribute)


def get_attribute(
    obj: object,
    attribute: str,
    default: Any = None,
) -> Any:
    """
    Safely retrieve an attribute.
    """
    return getattr(obj, attribute, default)
