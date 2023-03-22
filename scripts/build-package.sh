#!/bin/bash -e

python setup.py bdist_wheel
twine check dist/* --strict
