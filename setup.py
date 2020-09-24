from setuptools import find_packages, setup

setup(
    name='bilde-ord',
    version='0.1.0',
    description='Labeling objects in pictures.',
    author='Diana Spencer',
    url='https://github.com/dianaspencer/bilde-ord',
    license='MIT',
    packages=find_packages(exclude=('tests',))
)
