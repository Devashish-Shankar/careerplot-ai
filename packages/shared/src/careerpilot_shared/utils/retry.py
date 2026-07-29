"""
==========================================================
CareerPilot AI

Shared Package

Retry Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import time
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def retry(
    *,
    attempts: int = 3,
    delay: float = 1.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Retry a function if it raises one of the specified exceptions.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception: Exception | None = None

            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)

                except exceptions as exc:
                    last_exception = exc

                    if attempt == attempts - 1:
                        break

                    time.sleep(delay)

            assert last_exception is not None
            raise last_exception

        return wrapper

    return decorator


def exponential_backoff(
    attempt: int,
    *,
    base_delay: float = 1.0,
    factor: float = 2.0,
    max_delay: float = 60.0,
) -> float:
    """
    Calculate exponential backoff delay.
    """
    delay = base_delay * (factor ** max(0, attempt - 1))
    return min(delay, max_delay)
