import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Project"
AUTHOR_USER_NAME = "kushabhadra5"
SRC_REPO = "Project"
AUTHOR_EMAIL = "kushabhadra5@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "Python Package",
    long_description= longlong_description,
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where= "src")

)