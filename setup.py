import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hakYoutubeDownlaod", # Replace with your own username
    version="0.0.1",
    author="hakan ",
    author_email="hak122hak@gmail.com",
    description="Hızlı bir şekilde youtubeden videolar indirmek",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HAKANMAZI/hakYoutubeDownlaod",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)