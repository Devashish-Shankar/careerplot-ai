"""
==========================================================
CareerPilot AI

Shared Package

Version Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import platform
import sys


def python_version() -> str:
    """
    Return the current Python version.
    """
    return platform.python_version()


def python_implementation() -> str:
    """
    Return the Python implementation.
    """
    return platform.python_implementation()


def platform_name() -> str:
    """
    Return the operating system.
    """
    return platform.system()


def platform_release() -> str:
    """
    Return the operating system release.
    """
    return platform.release()


def executable() -> str:
    """
    Return the Python executable path.
    """
    return sys.executable
