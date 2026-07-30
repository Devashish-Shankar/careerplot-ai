"""
==========================================================
CareerPilot AI

Shared Package

Pagination Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import pytest
from careerpilot_shared.kernel import PageRequest, PageResult


def test_default_page_request() -> None:
    request = PageRequest()

    assert request.page == 1
    assert request.page_size == 20


def test_custom_page_request() -> None:
    request = PageRequest(
        page=2,
        page_size=50,
    )

    assert request.page == 2
    assert request.page_size == 50


@pytest.mark.parametrize(
    "page,page_size",
    [
        (0, 20),
        (-1, 20),
        (1, 0),
        (1, -5),
    ],
)
def test_invalid_page_request(
    page: int,
    page_size: int,
) -> None:
    with pytest.raises(ValueError):
        PageRequest(
            page=page,
            page_size=page_size,
        )


def test_empty_page_result() -> None:
    result = PageResult[int]()

    assert result.items == ()
    assert result.total == 0
    assert result.total_pages == 0
    assert not result.has_next
    assert not result.has_previous


def test_total_pages() -> None:
    result = PageResult[int](
        items=(1, 2, 3),
        total=95,
        page=1,
        page_size=10,
    )

    assert result.total_pages == 10


def test_has_next() -> None:
    result = PageResult[int](
        total=50,
        page=2,
        page_size=10,
    )

    assert result.has_next


def test_has_previous() -> None:
    result = PageResult[int](
        total=50,
        page=3,
        page_size=10,
    )

    assert result.has_previous


def test_last_page() -> None:
    result = PageResult[int](
        total=50,
        page=5,
        page_size=10,
    )

    assert not result.has_next
    assert result.has_previous