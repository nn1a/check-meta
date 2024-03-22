"""
xml to pydantic
"""

import os
import pathlib
from dataclasses import dataclass
from io import StringIO
from typing import Any, List, TypeVar

import dotenv
import xmltodict
from models import (
    candidate_snapshot,
    manifest,
    project_config,
    project_env,
    project_meta,
    snapshot_info,
)
from models.build_meta import BuildMeta

T = TypeVar("T")


@dataclass
class MetaFiles:
    """
    Test Case Data
    """

    filename: str
    force_list: tuple[str]
    model: T
    type: str


targets: List[MetaFiles] = [
    MetaFiles(
        filename="project_meta",
        force_list=project_meta.force_list,
        model=project_meta.ProjectMeta,
        type="xml",
    ),
    MetaFiles(
        filename="snapshot_info",
        force_list=snapshot_info.force_list,
        model=snapshot_info.SnapshotInfo,
        type="xml",
    ),
    MetaFiles(
        filename="candidate_snapshot",
        force_list=candidate_snapshot.force_list,
        model=candidate_snapshot.CandidateSnapshotInfo,
        type="xml",
    ),
    MetaFiles(
        filename="manifest.xml",
        force_list=manifest.force_list,
        model=manifest.Manifest,
        type="xml",
    ),
    MetaFiles(
        filename="project_env",
        force_list=None,
        model=project_env.ProjectEnv,
        type="env",
    ),
    MetaFiles(
        filename="project_config",
        force_list=None,
        model=project_config.ProjectConfig,
        type="text",
    ),
]


def load_model(data: str, target: MetaFiles) -> Any:
    """
    data to model
    """
    if target.type == "xml":
        parsed = xmltodict.parse(data, force_list=target.force_list, attr_prefix="")
        try:
            return target.model(**next(iter(parsed.values())))
        except Exception as e:
            raise e
    if target.type == "env":
        try:
            env = dotenv.main.DotEnv("", stream=StringIO(data))
            return target.model(env=env.dict())
        except Exception as e:
            raise e
    if target.type == "text":
        try:
            return target.model(config=data)
        except Exception as e:
            raise e
    raise RuntimeError(f"unknown type: {target.type}")


def load_models(meta_dir: str, project: str, detail: bool) -> BuildMeta:
    """
    do load_models
    """
    print(f"[TESTING] {project}")
    build_meta = {}
    for target in targets:
        filename = os.path.join(meta_dir, project, target.filename)
        if pathlib.Path(filename).exists():
            try:
                model = load_model(
                    pathlib.Path(filename).read_text(encoding="utf-8"), target
                )
                print(f"[PASS]: {project} {filename}")
                build_meta[target.filename] = model
                if detail:
                    print(model)
            except Exception as e:
                print(f"[FAIL]: {project} {filename}")
                raise e
        else:
            print(f"NOT PROJECT {project} {filename}")

    data = BuildMeta(
        name=project.split("/")[-1],
        meta_vcs="qb",
        path=project,
        project_meta=build_meta["project_meta"],
        project_config=build_meta["project_config"],
        project_env=build_meta["project_env"],
        snapshot_info=build_meta["snapshot_info"],
        candidate_snapshot=build_meta["candidate_snapshot"],
    )
    return data
