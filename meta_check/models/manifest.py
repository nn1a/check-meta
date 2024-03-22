"""
This module provides classes for validating data using Pydantic and typing.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class Remote(BaseModel):
    """
    manifest remote
    """

    name: str = Field(default="")
    fetch: str = Field(default="")
    review: str = Field(default="")


class Default(BaseModel):
    """
    manifest default
    """

    revision: str = Field(default="")
    remote: str = Field(default="")
    sync: str = Field(default="")
    sync_j: str = Field(default="", alias="sync-j")


class Reference(BaseModel):
    """
    manifest reference
    """

    project: str = Field(default="")
    url: str = Field(default="")


class Project(BaseModel):
    """
    manifest project
    """

    name: str
    path: str
    revision: str
    group: Optional[str] = Field(default="")
    remote: Optional[str] = Field(default="")


class Manifest(BaseModel):
    """
    manifest
    """

    remote: List[Remote] = Field(default=None)
    default: Optional[Default] = Field(default=None)
    reference: Optional[Reference] = Field(default=None)
    project: List[Project]


force_list = (
    "remote",
    "project",
)
