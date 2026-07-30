"""
==========================================================
CareerPilot AI

Shared Package

Specification Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import pytest
from careerpilot_shared.kernel import Specification


class EvenSpecification(Specification[int]):
    def is_satisfied_by(self, candidate: int) -> bool:
        return candidate % 2 == 0


class PositiveSpecification(Specification[int]):
    def is_satisfied_by(self, candidate: int) -> bool:
        return candidate > 0


def test_specification_subclass_is_callable() -> None:
    spec = EvenSpecification()

    assert spec(2)
    assert not spec(3)


def test_and_specification() -> None:
    spec = EvenSpecification().and_(PositiveSpecification())

    assert spec(4)
    assert not spec(-4)
    assert not spec(3)


def test_or_specification() -> None:
    spec = EvenSpecification().or_(PositiveSpecification())

    assert spec(4)
    assert spec(3)
    assert not spec(-3)


def test_not_specification() -> None:
    spec = EvenSpecification().not_()

    assert spec(3)
    assert not spec(2)


def test_nested_specification() -> None:
    spec = (
        EvenSpecification()
        .and_(PositiveSpecification())
        .not_()
    )

    assert spec(-2)
    assert spec(3)
    assert not spec(2)


def test_specification_is_abstract() -> None:
    with pytest.raises(TypeError):
        Specification()  # pyright: ignore[reportAbstractUsage]