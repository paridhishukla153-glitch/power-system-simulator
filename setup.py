from setuptools import setup, find_packages

setup(
    name="power-system-simulator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scipy",
        "networkx",
        "flask",
        "pytest",
        "openpyxl"
    ],
    python_requires=">=3.10",
)