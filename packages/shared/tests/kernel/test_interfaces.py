"""
==========================================================
CareerPilot AI

Shared Package

Interfaces Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

from careerpilot_shared.kernel import Auditable, HasIdentity, HasTimestamp, Identity, Serializable


@dataclass
class DummyIdentity:
    id: Identity


@dataclass
class DummyTimestamp:
    created_at: datetime
    updated_at: datetime


@dataclass
class DummySerializable:
    def to_dict(self) -> dict[str, Any]:
        return {"status": "ok"}


@dataclass
class DummyAuditable:
    created_by: Identity
    updated_by: Identity


def test_has_identity_protocol() -> None:
    obj = DummyIdentity(id=Identity.generate())

    assert isinstance(obj, HasIdentity)


def test_has_timestamp_protocol() -> None:
    now = datetime.now(UTC)

    obj = DummyTimestamp(
        created_at=now,
        updated_at=now,
    )

    assert isinstance(obj, HasTimestamp)


def test_serializable_protocol() -> None:
    obj = DummySerializable()

    assert isinstance(obj, Serializable)
    assert obj.to_dict() == {"status": "ok"}


def test_auditable_protocol() -> None:
    identity = Identity.generate()

    obj = DummyAuditable(
        created_by=identity,
        updated_by=identity,
    )

    assert isinstance(obj, Auditable)


def test_protocols_are_runtime_checkable() -> None:
    identity = Identity.generate()
    now = datetime.now(UTC)

    class CompleteObject:
        def __init__(self) -> None:
            self.id = identity
            self.created_at = now
            self.updated_at = now
            self.created_by = identity
            self.updated_by = identity

        def to_dict(self) -> dict[str, Any]:
            return {"id": str(self.id)}

    obj = CompleteObject()

    assert isinstance(obj, HasIdentity)
    assert isinstance(obj, HasTimestamp)
    assert isinstance(obj, Serializable)
    assert isinstance(obj, Auditable)