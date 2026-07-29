"""
==========================================================
CareerPilot AI

Shared Package

Common Enums

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from enum import StrEnum, auto


class Environment(StrEnum):
    """
    Application environments.
    """

    DEVELOPMENT = auto()
    TESTING = auto()
    STAGING = auto()
    PRODUCTION = auto()


class LogLevel(StrEnum):
    """
    Logging levels.
    """

    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()


class SortOrder(StrEnum):
    """
    Sort order.
    """

    ASC = auto()
    DESC = auto()


class Status(StrEnum):
    """
    Generic object status.
    """

    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()
    DISABLED = auto()
