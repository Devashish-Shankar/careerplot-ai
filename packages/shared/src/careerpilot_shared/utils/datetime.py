"""
==========================================================
CareerPilot AI

Shared Package

Datetime Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta


def utc_now() -> datetime:
    """
    Return the current UTC datetime.
    """
    return datetime.now(UTC)


def utc_today() -> datetime:
    """
    Return today's UTC date at midnight.
    """
    now = utc_now()

    return datetime(
        year=now.year,
        month=now.month,
        day=now.day,
        tzinfo=UTC,
    )


def to_iso(value: datetime) -> str:
    """
    Convert a datetime to an ISO-8601 string in UTC.
    """
    return value.astimezone(UTC).isoformat()


def from_iso(value: str) -> datetime:
    """
    Parse an ISO-8601 datetime string.
    """
    dt = datetime.fromisoformat(value)

    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)

    return dt.astimezone(UTC)


def is_expired(expires_at: datetime) -> bool:
    """
    Return True if the supplied datetime has passed.
    """
    return utc_now() >= expires_at.astimezone(UTC)


def seconds_from_now(seconds: int) -> datetime:
    """
    Return a UTC datetime after the specified number of seconds.
    """
    return utc_now() + timedelta(seconds=seconds)


def minutes_from_now(minutes: int) -> datetime:
    """
    Return a UTC datetime after the specified number of minutes.
    """
    return utc_now() + timedelta(minutes=minutes)


def hours_from_now(hours: int) -> datetime:
    """
    Return a UTC datetime after the specified number of hours.
    """
    return utc_now() + timedelta(hours=hours)


def days_from_now(days: int) -> datetime:
    """
    Return a UTC datetime after the specified number of days.
    """
    return utc_now() + timedelta(days=days)


def add_seconds(
    value: datetime,
    seconds: int,
) -> datetime:
    """
    Add seconds to a datetime.
    """
    return value + timedelta(seconds=seconds)


def add_minutes(
    value: datetime,
    minutes: int,
) -> datetime:
    """
    Add minutes to a datetime.
    """
    return value + timedelta(minutes=minutes)


def add_hours(
    value: datetime,
    hours: int,
) -> datetime:
    """
    Add hours to a datetime.
    """
    return value + timedelta(hours=hours)


def add_days(
    value: datetime,
    days: int,
) -> datetime:
    """
    Add days to a datetime.
    """
    return value + timedelta(days=days)


def duration(
    start: datetime,
    end: datetime,
) -> timedelta:
    """
    Return the duration between two datetimes.
    """
    return end - start


def age_in_days(value: datetime) -> int:
    """
    Return the age of a datetime in days.
    """
    return (utc_now() - value.astimezone(UTC)).days
