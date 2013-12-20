from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='bhlog',
    version=version,
    author='Bogdan Hodorog',
    author_email='bogdan.hodorog@gmail.com',
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    include_package_data=True,
)
