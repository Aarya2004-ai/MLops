from setuptools import find_packages,setup
from typing import List
# HYPHEN_DOT_E="-e ."
# def get_requirement(file_path:str)->List[str]:
#     requirement=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n", " ") for req in requirements ]
#         if HYPHEN_DOT_E in requirements:
#             requirements.remove(HYPHEN_DOT_E)
#     return requirements     
# setup(
# name='MLopsProject',
# version='0.0.1',
# author='Aarya_S',
# author_email='rya72004@gmail.com',
# packages=get_requirement(where='src'),
# package_dir={"":"src"},
# install_requires=get_requirement('requirements.txt'))
print(find_packages(where="src"))