from setuptools import setup, find_packages

setup(
    name='match_lib_package',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add any dependencies here, e.g., 'numpy'
    ],
    author='Hauke Heeren',
    author_email='heeren@match.uni-hannover.de',
    description='A Python library for match robots and other things, integrated with ROS.',
    license='MIT',
    keywords='ROS Python match robots',
    classifiers=[
        'Programming Language :: Python',
    ],
)