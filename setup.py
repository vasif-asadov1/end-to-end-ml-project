from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list:
    """Reads the requirements.txt file and returns a list of dependencies."""

    requirements = []
    with open(file_path, encoding="utf-8") as file_obj:
        for line in file_obj:
            requirement = line.strip()

            # Ignore comments, blank lines, and editable installs.
            if not requirement or requirement.startswith("#") or requirement.startswith("-e "):
                continue

            requirements.append(requirement)
 
    return requirements

setup(
    name="end-to-end-ml-project",
    version="0.1.0",
    author="Vasif",
    description="A complete end-to-end machine learning project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)