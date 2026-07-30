"""
==========================================================
CareerPilot AI

Shared Package

Repository Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from abc import abstractmethod

import pytest
from careerpilot_shared.kernel import Entity, Identity, PageRequest, PageResult, Repository


class User(Entity):
    pass


class UserRepository(Repository[User]):
    @abstractmethod
    def get(
        self,
        identity: Identity,
    ) -> User:
        ...

    @abstractmethod
    def get_or_none(
        self,
        identity: Identity,
    ) -> User | None:
        ...

    @abstractmethod
    def add(
        self,
        entity: User,
    ) -> None:
        ...

    @abstractmethod
    def update(
        self,
        entity: User,
    ) -> None:
        ...

    @abstractmethod
    def remove(
        self,
        entity: User,
    ) -> None:
        ...

    @abstractmethod
    def exists(
        self,
        identity: Identity,
    ) -> bool:
        ...

    @abstractmethod
    def count(self) -> int:
        ...

    @abstractmethod
    def list(self) -> tuple[User, ...]:
        ...

    @abstractmethod
    def page(
        self,
        request: PageRequest,
    ) -> PageResult[User]:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...


def test_repository_subclass_is_abstract() -> None:
    with pytest.raises(TypeError):
        UserRepository()  # type: ignore[abstract]


def test_repository_has_get_method() -> None:
    assert callable(UserRepository.get)


def test_repository_has_get_or_none_method() -> None:
    assert callable(UserRepository.get_or_none)


def test_repository_has_add_method() -> None:
    assert callable(UserRepository.add)


def test_repository_has_update_method() -> None:
    assert callable(UserRepository.update)


def test_repository_has_remove_method() -> None:
    assert callable(UserRepository.remove)


def test_repository_has_exists_method() -> None:
    assert callable(UserRepository.exists)


def test_repository_has_count_method() -> None:
    assert callable(UserRepository.count)


def test_repository_has_list_method() -> None:
    assert callable(UserRepository.list)


def test_repository_has_page_method() -> None:
    assert callable(UserRepository.page)


def test_repository_has_clear_method() -> None:
    assert callable(UserRepository.clear)