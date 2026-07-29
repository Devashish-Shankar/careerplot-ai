"""
==========================================================
CareerPilot AI

Shared Package

Import Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import importlib
from typing import Any


def import_module(name: str) -> Any:
    """
    Dynamically import a module.
    """
    return importlib.import_module(name)


def import_object(
    module: str,
    attribute: str,
) -> Any:
    """
    Import an object from a module.
    """
    imported = importlib.import_module(module)
    return getattr(imported, attribute)
