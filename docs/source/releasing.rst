***********************
Releasing a new version
***********************

Steps
=====

1. Remove previous build directories

.. code:: shell

    rm -rf build dist

2. Update the version number in ``location_field/__init__.py``

3. Push changes to GitHub (Pull Request)

4. Create a new release on GitHub

5. Build the package

.. code:: shell

    python -m build

6. Upload the package to PyPI

.. code:: shell

    python -m twine upload dist/*
