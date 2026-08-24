from setuptools import setup, find_packages

setup(
    name="aquamarine-dredge",
    version="1.0.1",
    packages=find_packages(),
    include_package_data=True,
    py_modules=["dredge_cli"] if "dredge_cli.py" in __import__('os').listdir('.') else [],
    install_requires=[
        "numpy",
        "pandas"
    ],
    extras_require={
        "ml": ["torch"],
        "full": ["torch", "pytest", "streamlit"],
    },
    entry_points={
        "console_scripts": [
            "aquamarine-dredge=dredge.cli:main" if "dredge" in __import__('os').listdir('.') else "aquamarine-dredge=dredge_cli:main",
            "dredge=dredge.cli:main" if "dredge" in __import__('os').listdir('.') else "dredge=dredge_cli:main",
        ],
    },
)
