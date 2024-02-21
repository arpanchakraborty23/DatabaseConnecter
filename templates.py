import os
from pathlib import Path
import logging

package_name="mongodb_connect"

list_of_files=[
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "test/unit/__init__.py",
    "test/unit/unit.py",
    "test/intregration/__init__.py",
    "test/intregration/int.py",
    "__init__setup.sh",
    "requirementes.txt",
    "requirementes_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiment.ipynb"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
          