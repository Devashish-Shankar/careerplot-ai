"""
==========================================================
CareerPilot AI

Shared Package Tests

Domain Event Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from careerpilot_shared.kernel import DomainEvent, Identity


def test_domain_event_creation() -> None:
    aggregate = Identity.generate()

    event = DomainEvent(
        aggregate_id=aggregate,
    )

    assert event.aggregate_id == aggregate
    assert event.event_version == 1
    assert event.payload == {}


def test_event_name() -> None:
    event = DomainEvent(
        aggregate_id=Identity.generate(),
    )

    assert event.event_name == "DomainEvent"


def test_event_has_event_id() -> None:
    event = DomainEvent(
        aggregate_id=Identity.generate(),
    )

    assert event.event_id is not None


def test_to_dict_contains_expected_keys() -> None:
    event = DomainEvent(
        aggregate_id=Identity.generate(),
        payload={"status": "created"},
    )

    data = event.to_dict()

    assert data["event_name"] == "DomainEvent"
    assert data["event_version"] == 1
    assert data["payload"] == {"status": "created"}

    assert "event_id" in data
    assert "aggregate_id" in data
    assert "occurred_at" in data