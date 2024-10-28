import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-NLP"
AUTH_USER_NAME = "SomyaPadhy4501"
SRC__REPO = "textSummarizer"
AUTHOR_EMAIL = "somyapadhy4501@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTH_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Text Summarization pipeline using BERT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SomyaPadhy4501/" + REPO_NAME,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
