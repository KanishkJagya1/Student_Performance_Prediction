from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirement(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='student_performance_prediction',
    version='0.0.1',
    author='Kanishk_Jagya',
    author_email='kjagya_be22@thapar.edu',
    packages=find_packages(),
    install_requires = ['pandas','numpy','seaborn']
)