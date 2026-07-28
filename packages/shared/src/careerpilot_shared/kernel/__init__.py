"""
==========================================================
CareerPilot AI

Shared Package

Kernel

Public exports for the Kernel package.

Author: Devashish Shankar
==========================================================
"""

from .agreegate_root import AggregateRoot
from .clock import Clock, SystemClock
from .domain_event import DomainEvent
from .entity import Entity
from .identity import Identity
from .interfaces import (
    Auditable,
    HasIdentity,
    HasTimestamp,
    Serializable,
)
from .pagination import PageRequest, PageResult
from .repository import Repository
from .specification import (
    AndSpecification,
    NotSpecification,
    OrSpecification,
    Specification,
)
from .unit_of_work import UnitOfWork

__all__ = [
    "AggregateRoot",
    "AndSpecification",
    "Auditable",
    "Clock",
    "DomainEvent",
    "Entity",
    "HasIdentity",
    "HasTimestamp",
    "Identity",
    "NotSpecification",
    "OrSpecification",
    "PageRequest",
    "PageResult",
    "Repository",
    "Serializable",
    "Specification",
    "SystemClock",
    "UnitOfWork",
]
