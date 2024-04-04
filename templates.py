import logging
import os
from pathlib import Path

project = "cyber_bullying"

paths = [
    ".github/workflow/.gitkeep",
    f"src/{project}/__init__.py",
    f"src/{project}/components/__init__.py",
    f"src/{project}/utils/__init__.py",
    f"src/{project}/utils/common.py",
    # f"src/{project}/clog/__init__.py",
    f"src/{project}/logging/__init__.py",
    f"src/{project}/config/__init__.py",
    f"src/{project}/config/configuration.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/entity/__init__.py",
    f"src/{project}/constants/__init__.py",
    "config/config.yaml",
    "research/notebooks/test.ipynb",
    "params.yaml",
    "app.py",
    "main.py",
    "setup.py",
    "DockerFile",
    "requirements.txt",
]

for path in paths:
    filepath = Path(path)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Directory created {filedir}")

    if not os.path.exists(path):
        open(path,'w')
        logging.info('file created',path)
    