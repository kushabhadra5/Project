import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s || %(levelname)s || %(message)s]'
)

while True:
    project_name = input("Enter Project name: ")
    if project_name !='':
        break

logging.info(f'Creating project: {project_name}')

#Creating list of files required for the project
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating file directory : {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    
    else:
        logging.info(f"File already present: {filename}")