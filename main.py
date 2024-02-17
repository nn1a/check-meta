"""
xml to pydantic
"""

import argparse
import os
import pathlib
from dataclasses import dataclass
from typing import List, TypeVar

import xmltodict

from models import candidate_snapshot, project_meta, snapshot_info

T = TypeVar("T")


@dataclass
class TestXml:
    """
    Test Case Data
    """

    filename: str
    force_list: tuple[str]
    model: T


targets: List[TestXml] = [
    {
        "filename": "project_meta",
        "force_list": project_meta.force_list,
        "model": project_meta.Project,
    },
    {
        "filename": "snapshot_info",
        "force_list": snapshot_info.force_list,
        "model": snapshot_info.SnapshotInfo,
    },
    {
        "filename": "candidate_snapshot",
        "force_list": candidate_snapshot.force_list,
        "model": candidate_snapshot.SnapshotInfo,
    },
]


def load_model(xml_data: dict, target: TestXml):
    """
    xml dict to model
    """
    parsed = xmltodict.parse(xml_data, force_list=target["force_list"], attr_prefix="")
    try:
        return target["model"](**next(iter(parsed.values())))
    except Exception as e:
        raise e


def list_directories(root_dir, depth=3):
    """
    get project meta directories
    """
    result = []
    for dirpath, dirnames, _ in os.walk(root_dir):
        current_depth = dirpath[len(root_dir) + 1 :].count(os.sep)
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if current_depth == depth - 1:
            result.append(dirpath[len(root_dir) + 1 :])
    return result


def test(meta_dir, detail):
    """
    do test
    """
    projects = list_directories(meta_dir, 3)
    for project in projects:
        print(f"[TESTING] {project}")
        for target in targets:
            filename = os.path.join(meta_dir, project, target["filename"])
            if pathlib.Path(filename).exists():
                try:
                    model = load_model(
                        pathlib.Path(filename).read_text(encoding="utf-8"), target
                    )
                    print(f"[PASS]: {project} {filename}")
                    if detail:
                        print(model)
                except Exception as e:
                    print(f"[FAIL]: {project} {filename}")
                    raise e
            else:
                print(f"NOT PROJECT{project} {filename}")


def parse_args():
    """command line option"""
    parser = argparse.ArgumentParser()
    parser.add_argument("meta", default="./qb", help="meta directory path")
    parser.add_argument(
        "-d", "--detail", default=False, action="store_true", help="Print detail"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    test(args.meta, args.detail)
