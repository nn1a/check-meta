"""
This module provides classes for validating data using Pydantic and typing.
"""

from typing import List

from pydantic import BaseModel


class Repository(BaseModel):
    """
    snapshot repository
    """

    name: str
    type: dict


class Base(BaseModel):
    """
    base snapshot
    """

    target: str
    url: str
    repository: List[Repository]


class SnapshotInfo(BaseModel):
    """
    current snapshot information
    """

    latest: dict
    reference: dict
    base: List[Base]


force_list = (
    "base",
    "repository",
)
