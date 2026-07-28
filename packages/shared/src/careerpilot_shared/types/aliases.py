"""
==========================================================
CareerPilot AI

Shared Package

Common Type Aliases

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

type PathLike = str | Path

type Metadata = dict[str, Any]

type Headers = dict[str, str]

type QueryParams = dict[str, str]

type StringMap = dict[str, str]

type AnyMap = dict[str, Any]