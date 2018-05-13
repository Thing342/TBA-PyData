from setuptools import setup

setup(
    name='tba-pydata',
    version='0.1.1',
    packages=['tba_pydata', 'tba_pydata.games'],
    url='https://github.com/Thing342/TBA-PyData',
    license='MIT',
    author='Wes Jordan',
    author_email='wes@wesj.org',
    description='Wrapper for working with the Blue Alliance API in pandas',

    keywords=['thebluealliance', 'frc', 'pydata', 'tba'],

    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    install_requires = [
        'numpy',
        'requests',
        'pandas',
        'statsmodels'
    ]
)
