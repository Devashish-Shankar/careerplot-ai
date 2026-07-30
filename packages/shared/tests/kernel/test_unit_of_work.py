"""
==========================================================
CareerPilot AI

Shared Package

Unit Of Work Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import pytest
from careerpilot_shared.kernel import UnitOfWork


class FakeUnitOfWork(UnitOfWork):
    def __init__(self) -> None:
        self.calls: list[str] = []

    def begin(self) -> None:
        self.calls.append("begin")

    def commit(self) -> None:
        self.calls.append("commit")

    def rollback(self) -> None:
        self.calls.append("rollback")

    def flush(self) -> None:
        self.calls.append("flush")

    def close(self) -> None:
        self.calls.append("close")


def test_unit_of_work_is_abstract() -> None:
    with pytest.raises(TypeError):
        UnitOfWork()  # pyright: ignore[reportAbstractUsage]


def test_context_manager_commit() -> None:
    uow = FakeUnitOfWork()

    with uow:
        pass

    assert uow.calls == [
        "begin",
        "commit",
        "close",
    ]


def test_context_manager_rollback() -> None:
    uow = FakeUnitOfWork()

    with pytest.raises(RuntimeError):
        with uow:
            raise RuntimeError()

    assert uow.calls == [
        "begin",
        "rollback",
        "close",
    ]


def test_flush() -> None:
    uow = FakeUnitOfWork()

    uow.flush()

    assert uow.calls == [
        "flush",
    ]


def test_manual_commit() -> None:
    uow = FakeUnitOfWork()

    uow.begin()
    uow.commit()
    uow.close()

    assert uow.calls == [
        "begin",
        "commit",
        "close",
    ]


def test_manual_rollback() -> None:
    uow = FakeUnitOfWork()

    uow.begin()
    uow.rollback()
    uow.close()

    assert uow.calls == [
        "begin",
        "rollback",
        "close",
    ]