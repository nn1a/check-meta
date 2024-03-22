"""
This module provides classes for validating data using Pydantic and typing.
"""

from typing import List, Optional

from pydantic import BaseModel


class Arch(BaseModel):
    """architecutre"""

    name: str


class Image(BaseModel):
    """image ks filename"""

    name: str


class Path(BaseModel):
    "path project - ngbs only"
    project: str
    repository: str


class Repository(BaseModel):
    """
    repository
    """

    name: str
    path: Optional[List[Path]] = None
    arch: List[Arch]
    image: Optional[List[Image]] = None


class Branch(BaseModel):
    """branch information"""

    name: str


class Org(BaseModel):
    """branch mapping org"""

    name: str
    branch: List[Branch]


class BranchCandidate(BaseModel):
    """branch mapping"""

    name: str
    default: Optional[str]
    org: List[Org]


class Package(BaseModel):
    """abs package"""

    repo: str


class Packages(BaseModel):
    """abs packages"""

    package: List[Package]


class Rootstrap(BaseModel):
    """abs rootstrap"""

    url: str


class Branches(BaseModel):
    """abs branch"""

    source: str
    output: str


class Abs(BaseModel):
    """abs"""

    branch: List[Branches]
    rootstrap: Rootstrap
    packages: Packages


class AbsConfig(BaseModel):
    """abs config"""

    abs: List[Abs]


class DebugInfo(BaseModel):
    """debuginfo"""

    enable: Optional[str] = None
    disable: Optional[str] = None


class UseImgAddrm(BaseModel):
    """
    images add remove feature
    """

    enable: Optional[str] = None
    disable: Optional[str] = None


class Maintainers(BaseModel):
    """
    project maintainers
    """

    def __init__(self, **kwargs):
        project_leader = kwargs.get("project_leader")
        if project_leader is None:
            kwargs["project_leader"] = []
        elif isinstance(project_leader, list):
            new_items = []
            for item in project_leader:
                if item is not None:
                    new_items.append(item)
            kwargs["project_leader"] = new_items
        super().__init__(**kwargs)

    project_leader: Optional[List[str]]


class ProjectMeta(BaseModel):
    """
    project
    """

    name: str
    debuginfo: DebugInfo
    repository: List[Repository]
    branch_candidate: List[BranchCandidate]
    abs_config: Optional[AbsConfig] = None
    use_img_addrm: UseImgAddrm
    maintainers: Maintainers


force_list = (
    "repository",
    "path",
    "branch_candidate",
    "arch",
    "image",
    "org",
    "branch",
    "abs",
    "package",
    "project_leader",
)
