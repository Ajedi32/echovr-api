import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="echovr_api",
    version="0.2.0",
    author="Ajedi32",
    author_email="ajedi32.web@gmail.com",
    description="Python bindings for Echo VR's HTTP API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ajedi32/echovr-api/",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests"
    ],
    extras_require={
        'docs': [
            'sphinx >=1.8.2, <2.0.0a0',
            'sphinx-autodoc-typehints >=1.5.0, <2.0.0a0',
            'sphinxcontrib-apidoc >=0.3.0, <0.4.0a0',
            'm2r >=0.2.1, <0.3.0a0',
            'sphinx_rtd_theme >=0.4.2, <0.5.0a0',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
    ],
)
