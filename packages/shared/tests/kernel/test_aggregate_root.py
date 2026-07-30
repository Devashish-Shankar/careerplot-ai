"""
==========================================================
CareerPilot AI

Shared Package Tests

Aggregate Root Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from careerpilot_shared.kernel import AggregateRoot, DomainEvent


@dataclass(eq=False)
class User(AggregateRoot):
    name: str = "Devashish"


def make_event(user: User) -> DomainEvent:
    return DomainEvent(
        aggregate_id=user.id,
        payload={"name": user.name},
    )


def test_no_events_initially() -> None:
    user = User()

    assert not user.has_domain_events
    assert user.domain_events == ()


def test_add_domain_event() -> None:
    user = User()

    event = make_event(user)

    user.add_domain_event(event)

    assert user.has_domain_events
    assert len(user.domain_events) == 1
    assert user.domain_events[0] == event


def test_pull_domain_events() -> None:
    user = User()

    event = make_event(user)

    user.add_domain_event(event)

    events = user.pull_domain_events()

    assert len(events) == 1
    assert events[0] == event
    assert not user.has_domain_events


def test_clear_domain_events() -> None:
    user = User()

    user.add_domain_event(make_event(user))
    user.add_domain_event(make_event(user))

    assert user.has_domain_events

    user.clear_domain_events()

    assert user.domain_events == ()
    assert not user.has_domain_events