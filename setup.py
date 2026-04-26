from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT_E = "-e ."

def get_requirement(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith("#") and line != HYPHEN_DOT_E:
                requirements.append(line)
    return requirements

setup(
    name='MLopsProject',
    version='0.0.1',
    author='Aarya_S',
    author_email='rya72004@gmail.com',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=get_requirement('requirements.txt'),
)