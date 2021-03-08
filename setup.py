import setuptools


with open("README.md", "r") as setup:
    long_description = setup.read()

setuptools.setup(
    name="mygtu",
    version="0.1.15",
    author="g",
    author_email="k",
    description="g",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/batatavadaX/testgtu",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    # data_files=[('mygtu', ['mygtu/database/*.json'])], 
    install_requires=['datetime', 'pytz', 'ujson'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
