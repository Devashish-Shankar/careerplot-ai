"""
==========================================================
CareerPilot AI

Shared Package Tests

Entity Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from careerpilot_shared.kernel import Entity, Identity


@dataclass(eq=False)
class User(Entity):
    name: str = "Devashish"


def test_entity_has_identity() -> None:
    user = User()

    assert isinstance(user.id, Identity)
    assert user.identity == user.id


def test_entities_are_equal_when_identity_matches() -> None:
    identity = Identity.generate()

    left = User(id=identity)
    right = User(id=identity)

    assert left == right


def test_entities_are_not_equal_when_identity_differs() -> None:
    left = User()
    right = User()

    assert left != right


def test_hash_uses_identity() -> None:
    user = User()

    assert hash(user) == hash(user.id)


def test_repr_contains_class_name() -> None:
    user = User()

    assert "User" in repr(user)