import sys
from pathlib import Path


def use_project(scene_file):
    """Add this scene's project folder to Python's search path,
    so that `from symbols import *` finds projects/<name>/symbols.py."""
    here = Path(scene_file).resolve()
    for folder in here.parents:
        if folder.parent.name == "projects":
            sys.path.insert(0, str(folder))
            return folder
    return None