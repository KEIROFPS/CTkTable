from setuptools import setup, find_packages

setup(
    name="CTkTable",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "customtkinter",  # Ensure this is installed as a dependency
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    description="A Python package for CTkTable functionality",
    long_description="CTkTable is a simple table widget for use with the CustomTkinter library.",
    long_description_content_type="text/markdown",
    url="https://github.com/KEIROFPS/CTkTable",
    author="KEIROFPS",
    license="MIT",
)
