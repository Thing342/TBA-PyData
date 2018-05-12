# TBA-PyData

**Author:** Wes Jordan

**License:** MIT

**Latest Version:** 0.1.0a1 (under heavy development)

**Purpose:** To serve as a wrapper for the [The Blue Alliance](https://www.thebluealliance.com/) API for use with the 
PyData statistical stack. (Eg. `pandas`, `numpy`, etc)

## Features:
* Import live data from The Blue Alliance API into `pandas` DataFrames.
* Parallel multi-fetch for multi-part datasets (fetch the matches for an entire district, for example)
* Team number and region normalization
* Component OPR and EPR calculation via `statsmodels`.

## Requirements:
* Python **3.5** or greater.
* Some version of **pip** installed *(tested version is 9.0.1)*

## Installation:
This package is available on [PyPI](https://pypi.org/project/tba-pydata/), and can be installed via pip:
```sh
pip install tba-pydata
```

## Contributing:
This project uses [pipenv](https://github.com/pypa/pipenv) to manage development environments.
To set up a development environment, install pipenv, and in the root of the project, run:
```sh
pipenv install
pipenv shell
```
This will create a virtual environment with the project's dependencies.

