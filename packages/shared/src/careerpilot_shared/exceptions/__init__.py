"""
CareerPilot AI

Shared Exception Package
"""

from .authentication import AuthenticationError
from .authorization import AuthorizationError
from .base import CareerPilotError
from .conflict import ConflictError
from .domain import DomainError
from .infrastructure import InfrastructureError
from .not_found import NotFoundError
from .validation import ValidationError

__all__ = [
    "CareerPilotError",
    "ValidationError",
    "AuthenticationError",
    "AuthorizationError",
    "NotFoundError",
    "ConflictError",
    "DomainError",
    "InfrastructureError",
]
