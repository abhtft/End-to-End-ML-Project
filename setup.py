##used in machine learning application as a package itself

from setuptools import find_packages, setup
from typing import List

hypendot = '-e.'

def get_requirements(file_path: str) -> List[str]:
    # This function will return a list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Using strip() instead of replace()

        if hypendot in requirements:
            requirements.remove(hypendot)

    return requirements  # **Make sure to return the list**

setup(
    name='mlproject',
    version='0.0.1',
    author='Abhishek',
    author_email='abh.tft@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Ensure correct file name
)
