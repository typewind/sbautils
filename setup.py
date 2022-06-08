import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sbautlis",
    version="0.0.1",
    author="Typewind",
    author_email="indi@juntoalmanzanares.futbol",
    description="Personal Statsbomb data analysis utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/typewind/sbautils",
    project_urls={
        "Bug Tracker": "https://github.com/typewind/sbautils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)