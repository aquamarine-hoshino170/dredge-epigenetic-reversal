from setuptools import setup, find_packages

setup(
    name="aquamarine-dredge",
    version="24.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy"],
    entry_points={
        "console_scripts": [
            "aquamarine-dredge=dredge.cli:main",
            "dredge=dredge.cli:main",
        ],
    },
)
