"""
This module provides classes for validating data using Pydantic and typing.
"""

from pydantic import BaseModel

from .candidate_snapshot import CandidateSnapshotInfo
from .project_config import ProjectConfig
from .project_env import ProjectEnv
from .project_meta import ProjectMeta
from .snapshot_info import SnapshotInfo


class BuildMeta(BaseModel):
    """
    project env value
    """

    name: str
    meta_vcs: str
    path: str
    project_meta: ProjectMeta
    candidate_snapshot: CandidateSnapshotInfo
    snapshot_info: SnapshotInfo
    project_config: ProjectConfig
    project_env: ProjectEnv
