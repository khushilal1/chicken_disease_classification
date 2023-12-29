import setuptools

with open("README.md") as f:
    long_description = f.read()

__verson__ = "0.0.0"
REPO_NAME = "chicken_disease_classification"
AUTHOR_USERNAME = "khushilal"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mahatokhushila2019@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__verson__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small project for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_url={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME})/{REPO_NAME}/issue",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
