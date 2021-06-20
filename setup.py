from setuptools import setup, find_packages

with open('readme.md', 'r') as fob:
    long_description = fob.read()
with open('requirements.txt', 'r') as fob:
    requirements = fob.readlines()

setup(
    name='cns',
    version='1.0.0',
    author='Kenneth Sabalo',
    author_email='kennethsantanasablo@gmail.com',
    url='https://github.com/kendfss/cns',
    description="REPL for pythonic file system management and navigation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='utilities operating path file system local server web',
    license='GNU GPLv3',
    requires=requirements,
    entry_points={
        'console_scripts': [
            'cns = cns.cli:main'
        ]
    },
    python_requires='>=3.10',
)
