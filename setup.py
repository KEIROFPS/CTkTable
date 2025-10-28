from setuptools import setup, find_packages

setup(
    name="CTkTable",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "customtkinter",
    ],
    include_package_data=True,
)

