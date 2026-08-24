from setuptools import setup, find_packages

setup(
    name="dredge-epigenetic",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "torch",
        "pytest",
        "streamlit"
    ],
    entry_points={
        "console_scripts": [
            "dredge=dredge_cli:main",
        ],
    },
)
