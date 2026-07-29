"""
==========================================================
CareerPilot AI

Shared Package

State

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class State:
    """
    Generic mutable state object.
    """

    value: str

    def transition(self, value: str) -> None:
        """
        Transition to a new state.
        """
        self.value = value

    def __str__(self) -> str:
        return self.value
