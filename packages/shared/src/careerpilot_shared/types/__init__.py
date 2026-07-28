"""
==========================================================
CareerPilot AI

Shared Package

Types

Author: Devashish Shankar
==========================================================
"""

from .aliases import (
    AnyMap,
    Headers,
    Metadata,
    PathLike,
    QueryParams,
    StringMap,
)
from .identifiers import (
    AgentId,
    ApplicationId,
    CandidateId,
    CompanyId,
    DocumentId,
    InterviewId,
    JobId,
    NotificationId,
    ResumeId,
    UserId,
)
from .json import (
    JsonArray,
    JsonObject,
    JsonPrimitive,
    JsonValue,
)
from .primitives import (
    CountryCode,
    CurrencyCode,
    DirectoryPath,
    EmailAddress,
    FilePath,
    LanguageCode,
    MimeType,
    TimeZone,
    UrlString,
)
from .protocols import (
    SupportsFromDict,
    SupportsToDict,
)

__all__ = [
    "AgentId",
    "AnyMap",
    "ApplicationId",
    "CandidateId",
    "CompanyId",
    "CountryCode",
    "CurrencyCode",
    "DirectoryPath",
    "DocumentId",
    "EmailAddress",
    "FilePath",
    "Headers",
    "InterviewId",
    "JobId",
    "JsonArray",
    "JsonObject",
    "JsonPrimitive",
    "JsonValue",
    "LanguageCode",
    "Metadata",
    "MimeType",
    "NotificationId",
    "PathLike",
    "QueryParams",
    "ResumeId",
    "StringMap",
    "SupportsFromDict",
    "SupportsToDict",
    "TimeZone",
    "UrlString",
    "UserId",
]