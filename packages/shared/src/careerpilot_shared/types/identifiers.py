"""
==========================================================
CareerPilot AI

Shared Package

Identifier Type Aliases

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from typing import NewType

UserId = NewType("UserId", str)

CandidateId = NewType("CandidateId", str)

ResumeId = NewType("ResumeId", str)

ApplicationId = NewType("ApplicationId", str)

JobId = NewType("JobId", str)

CompanyId = NewType("CompanyId", str)

InterviewId = NewType("InterviewId", str)

NotificationId = NewType("NotificationId", str)

AgentId = NewType("AgentId", str)

DocumentId = NewType("DocumentId", str)