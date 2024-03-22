"""
This module provides classes for validating data using Pydantic and typing.
"""

from pydantic import BaseModel, Field


class ProjectConfig(BaseModel):
    """
    project env value
    """

    config: str = Field(default="")
