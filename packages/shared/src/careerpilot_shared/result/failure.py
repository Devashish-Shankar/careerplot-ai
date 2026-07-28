"""
==========================================================
CareerPilot AI

Shared Package

Failure Factory

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from .result import Result


def Failure(error: Exception) -> Result[object]:
    """
    Create a failed Result.

    Parameters
    ----------
    error:
        The exception describing the failure.

    Returns
    -------
    Result[T]
        A failed Result instance.
    """
    return Result(error=error)
