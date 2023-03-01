# datapca

[![GitHub tag](https://img.shields.io/github/v/tag/saastoolset/datapca)](https://github.com/saastoolset/datapca/tags)
[![development status](https://img.shields.io/badge/development%20status-pre--alpha-orange.svg)](https://pypi.org/project/datapca/)
[![supports](https://img.shields.io/pypi/pyversions/datapca.svg)](https://github.com/saastoolset/datapca/blob/master/pyproject.toml)
[![CI status](https://github.com/saastoolset/datapca/actions/workflows/check_code_quality.yml/badge.svg)](https://github.com/saastoolset/datapca/actions/workflows/check_code_quality.yml)
[![codecov](https://codecov.io/gh/saastoolset/datapca/branch/main/graphs/badge.svg)](https://codecov.io/github/saastoolset/datapca)


Data platform utility with Python Clean Architcture


* Documentation: <https://saastoolset.github.io/datapca>
* GitHub: <https://github.com/saastoolset/datapca>
* PyPI: <https://pypi.org/project/datapca/>
* Free software: [Apache-2.0](./LICENSE)


## Features

* [TBDL]

## I. The proposed environment setup
- conda as environment manager
- pypi/pip as package repository and manager 
- Poetry as the dependency manager.

https://ealizadeh.com/blog/guide-to-python-env-pkg-dependency-using-conda-poetry


## II. Environment prepare

### Virtual environment 

```
$ conda create -n datapca
$ activate datapca

```

### Install Poetry

```
conda install -c conda-forge poetry
```

Setup path 
```
$HOME/.local/bin for Unix
%APPDATA%\Python\Scripts on Windows
```


### poetry initial
```
$ poetry init
```
