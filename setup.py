from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements file and returns a list of dependencies."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # FIXED: `read_lines()` → `readlines()`
        requirements = [req.strip() for req in requirements]  # Removing newlines
    
    # Remove "-e ." if present
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="ml-project",
    version="0.0.1",
    author="arif",
    author_email="mohammedarifsn2@gmail.com",  # FIXED: Added missing comma
    packages=find_packages(),  # FIXED: Called `find_packages()`
    install_requires=get_requirements("requirements.txt")
)



