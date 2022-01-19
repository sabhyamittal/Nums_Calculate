from unicodedata import name
from setuptools import setup, find_packages

classifiers = [
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python '
]

setup(
    name= 'basiccalculator',
    version= '0.0.1',
    description='A very basic calculator', 
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='Sabhya Mittal',
    author_email = 'sabhyamittal26@gmail.com',
    url='https://github.com/sabhyamittal/Pypi/archive/refs/tags/0.0.1.tar.gz',
    packages=find_packages(),
    classifiers=classifiers,
    license='MIT',
    keywords='calculator',
    install_requires=['']
)
