from setuptools import setup, find_packages

# Read the requirements from requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="JarvisBot",  # Name of your project
    version="0.1.0",  # Version number
    author="Sumit Yadav",  # Your name
    author_email="sumityadav329@gmail.com",  # Your email
    description="A personalized home automation assistant.",  # Short description
    long_description=open("README.md").read(),  # Long description from README.md
    long_description_content_type="text/markdown",  # Type of long description
    url="https://github.com/sumityadav329/apnaJarvis.git",  # Project URL
    packages=find_packages(where="src"),  # Automatically find packages in the `src` directory
    package_dir={"": "src"},  # Specify that packages are in the `src` directory
    install_requires=requirements,  # Dependencies from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Minimum Python version required
    entry_points={
        "console_scripts": [
            "jarvis=main:main",  # Command-line entry point
        ],
    },
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
)