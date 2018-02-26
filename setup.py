from setuptools import setup, find_packages

__VERSION__ = '0.1'


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='p3common',
    version=__VERSION__,
    description='mischus - Python3 Common utility classes',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Python :: Common',
    ],
    url='https://github.com/mischuh/python3-common.git',
    author='Mirko Schuh',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        "decorator>=4.2.1",
    ],
    python_requires='>=3',
    include_package_data=True,
    zip_safe=False
)
