"""
==========================================================
CareerPilot AI

Shared Package Tests

Identity Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from careerpilot_shared.kernel import Identity


def test_generate_identity() -> None:
    identity = Identity.generate()

    assert isinstance(identity, Identity)


def test_generated_identities_are_unique() -> None:
    first = Identity.generate()
    second = Identity.generate()

    assert first != second


def test_from_string() -> None:
    identity = Identity.generate()

    recreated = Identity.from_string(str(identity))

    assert recreated == identity


def test_string_representation() -> None:
    identity = Identity.generate()

    assert str(identity)


def test_repr_contains_identity() -> None:
    identity = Identity.generate()

    assert "Identity" in repr(identity)