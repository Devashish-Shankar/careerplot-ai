"""
==========================================================
CareerPilot AI

Shared Package

Inspection Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import inspect
from collections.abc import Callable


def function_name(function: Callable[..., object]) -> str:
    """
    Return the function name.
    """
    return function.__name__


def is_async(function: Callable[..., object]) -> bool:
    """
    Determine whether a callable is asynchronous.
    """
    return inspect.iscoroutinefunction(function)


def signature(function: Callable[..., object]) -> inspect.Signature:
    """
    Return the function signature.
    """
    return inspect.signature(function)


def docstring(function: Callable[..., object]) -> str | None:
    """
    Return the function docstring.
    """
    return inspect.getdoc(function)
