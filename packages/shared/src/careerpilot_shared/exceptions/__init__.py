"""
CareerPilot AI

Shared Exception Package
"""

from .authentication import AuthenticationError
from .authorization import AuthorizationError
from .base import CareerPilotError
from .validation import ValidationError

__all__ = [
    "CareerPilotError",
    "ValidationError",
    "AuthenticationError",
    "AuthorizationError",
]