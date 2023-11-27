# MatchLib

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Python Library for match robots and other things.

## Getting Started <a name = "getting_started"></a>
Install venv with inherited packages from global interpreter:
```
python3 -m venv --system-site-packages venv
```

Use venv:
```bash
source ~/hee/venv/bin/activate
```

### Installing

Get most current match_lib submodule:

```bash
git submodule update --init --remote
```


Install package with connection to source (no reinstallation if changed):
```bash
pip install -e .
```

Add requirements for testing:
```bash
pip install -r requirements_dev.txt
```
## Usage <a name = "usage"></a>

Add notes about how to use the system.

### Testing
Run tests for code:
```bash
mypy src
flake8 src
pytest
```

In different env (not working right now):
```bash
tox
```
