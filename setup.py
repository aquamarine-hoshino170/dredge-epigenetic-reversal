from setuptools import setup, find_packages

setup(
    name="aquamarine-dredge",
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
            "aquamarine-dredge=dredge_cli:main",
            "dredge=dredge_cli:main",
        ],
    },
)
