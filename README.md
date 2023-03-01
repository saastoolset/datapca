# datapca
Data platform utility with Python Clean Architcture


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
