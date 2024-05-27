from setuptools import setup, find_packages

setup(
    name='Feather Logging',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
    extras_require={
        "yaml": ["yaml"]
    }
)
