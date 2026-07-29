"""
==========================================================
CareerPilot AI

Shared Package

Validation Utilities

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

import re
from uuid import UUID

from careerpilot_shared.constants import (
    EMAIL_REGEX,
    GITHUB_REGEX,
    LINKEDIN_REGEX,
    PHONE_REGEX,
    URL_REGEX,
)


def is_email(value: str) -> bool:
    """
    Validate an email address.
    """
    return (
        re.fullmatch(
            EMAIL_REGEX,
            value,
        )
        is not None
    )


def is_phone(value: str) -> bool:
    """
    Validate an international phone number.
    """
    return (
        re.fullmatch(
            PHONE_REGEX,
            value,
        )
        is not None
    )


def is_url(value: str) -> bool:
    """
    Validate a URL.
    """
    return (
        re.fullmatch(
            URL_REGEX,
            value,
        )
        is not None
    )


def is_linkedin_url(value: str) -> bool:
    """
    Validate a LinkedIn profile URL.
    """
    return (
        re.fullmatch(
            LINKEDIN_REGEX,
            value,
        )
        is not None
    )


def is_github_url(value: str) -> bool:
    """
    Validate a GitHub profile URL.
    """
    return (
        re.fullmatch(
            GITHUB_REGEX,
            value,
        )
        is not None
    )


def is_uuid(value: str) -> bool:
    """
    Validate a UUID string.
    """
    try:
        UUID(value)
    except ValueError:
        return False

    return True
