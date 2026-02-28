import setuptools

with open("README.md" , 'r',encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Kidney-Disease-classification-Project"
AUTHOR_NAME = "Santosh Singh"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "santosh102969@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description = "CNN Classifier",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker" : f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
)