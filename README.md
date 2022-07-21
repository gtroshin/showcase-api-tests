# Showcase API Tests

![Python 3.9.1](https://img.shields.io/badge/Python-3.9.1-green.svg)
[![Python Tests](https://github.com/gtroshin/showcase-api-tests/actions/workflows/python-unit-tests.yml/badge.svg)](https://github.com/gtroshin/showcase-api-tests/actions/workflows/python-unit-tests.yml)

Showcase API tests using a Python' `unittest` testing framework.

## Requirements

Install [Python 3.9.10](https://www.python.org/downloads/release/python-3910/).

Install dependencies:

    pip3.9 install -r requriments.txt

## Development

To run tests, use the following command:

    python3.9 -m unittest discover -s . -p "*_test.py" -v
