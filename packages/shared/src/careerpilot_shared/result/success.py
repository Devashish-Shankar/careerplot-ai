"""
==========================================================
CareerPilot AI

Shared Package

Success Factory

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .result import Result


def Success[T](value: T) -> Result[T]:
    """
    Create a successful Result.

    Parameters
    ----------
    value:
        The successful value.

    Returns
    -------
    Result[T]
        A successful Result instance.
    """
    return Result(value=value)