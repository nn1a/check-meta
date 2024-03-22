"""
xml to pydantic
"""

import argparse
import os

from loader import load_models


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
    projects = list_directories(meta_dir.rstrip("/"), 3)
    print(projects)
    for project in projects:
        load_models(meta_dir, project, detail)


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
