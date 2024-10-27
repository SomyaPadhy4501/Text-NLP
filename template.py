import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s:')

project_Name = 'textSummarizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_Name}/__init__.py",
    f"src/{project_Name}/components/__init__.py",
    f"src/{project_Name}/components/utils/__init__.py",
    f"src/{project_Name}/components/utils/common.py",
    f"src/{project_Name}/components/logging/__init__.py",
    f"src/{project_Name}/components/config/__init__.py",
    f"src/{project_Name}/components/config/configuration.py",
    f"src/{project_Name}/components/pipeline/__init__.py",
    f"src/{project_Name}/components/entity/__init__.py",
    f"src/{project_Name}/components/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Docketfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir , filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"File: {filepath} already exists.")

