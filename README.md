# gribby

[![Build Status](https://travis-ci.org/wmo-cop/gribby.png)](https://travis-ci.org/wmo-cop/gribby)

## Overview

gribby is a pure Python package implementing [WMO FM 92 GRIB Edition 3](https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/FM92-16-GRIB/FM-92-16_GRIB-edition-3_CBS-16.pdf)

## Installation

The easiest way to install gribby is via the Python [pip](https://pip.pypa.io/en/stable/)
utility:

```bash
pip install gribby
```

### Requirements
- Python 3
- [virtualenv](https://virtualenv.pypa.io/)

### Dependencies
Dependencies are listed in [requirements.txt](requirements.txt). Dependencies
are automatically installed during gribby installation.

### Installing gribby

```bash
# setup virtualenv
python -m venv gribby
cd gribby
source bin/activate

# clone codebase and install
git clone https://github.com/wmo-cop/gribby.git
cd gribby
python setup.py build
python setup.py install
```

## Running

TODO

### Using the API

TODO

## Development

### Running Tests

```bash
# install dev requirements
pip install -r requirements-dev.txt

# run tests like this:
python tests/run_tests.py

# or this:
python setup.py test
```

## Releasing

```bash
python setup.py sdist bdist_wheel --universal
twine upload dist/*
```

### Code Conventions

* [PEP8](https://www.python.org/dev/peps/pep-0008)

### Bugs and Issues

All bugs, enhancements and issues are managed on [GitHub](https://github.com/wmo-cop/gribby/issues).

## Contact

* [Tom Kralidis](https://github.com/tomkralidis)
