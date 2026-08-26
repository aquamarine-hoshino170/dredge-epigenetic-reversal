from setuptools import setup, find_packages

setup(
    name="aquamarine-dredge",
    version="115.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'aquamarine-dredge=dredge.cli:main',
        ],
    },
)
