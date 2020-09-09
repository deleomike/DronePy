import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DronePy", # Replace with your own username
    version="0.0.1",
    author="Michael DeLeo",
    author_email="michaeldeleo31@yahoo.com",
    description="An open source Hobbyist Drone Interface Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deleomike/DronePy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
