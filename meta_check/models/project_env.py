"""
This module provides classes for validating data using Pydantic and typing.
"""

from typing import Dict, Optional

from pydantic import BaseModel, Field


class ProjectEnv(BaseModel):
    """
    project env value
    """

    env: Optional[Dict] = Field(default={})
