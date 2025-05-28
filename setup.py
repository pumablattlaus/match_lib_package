from setuptools import setup, find_packages

# fetch values from package.xml
setup(
    name='match_lib_package',
    version="0.1.0",
    package_dir={'': 'src'},
    packages=find_packages("src"),
    install_requires=[
        'numpy'
        # …
    ],
)
