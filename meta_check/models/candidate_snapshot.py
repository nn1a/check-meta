"""
This module provides classes for validating data using Pydantic and typing.
"""

from typing import List

from pydantic import BaseModel


class Candidate(BaseModel):
    """
    candidate snapshot
    """

    target: str
    url: str


class BaseCandidate(BaseModel):
    """
    candidate base snapshot
    """

    target: str
    url: str


class CandidateSnapshotInfo(BaseModel):
    """
    snapshot list
    """

    candidate: List[Candidate]
    base_candidate: List[BaseCandidate]


force_list = (
    "candidate",
    "base_candidate",
)
