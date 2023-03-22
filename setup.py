from setuptools import find_packages, setup

VERSION = __import__("location_field").__version__


setup(
    name="django-location-field",
    version=VERSION,
    description="Location field for Django",
    long_description="This module provides a location field for Django applications.",
    long_description_content_type="text/x-rst",
    author="Caio Ariede",
    author_email="caio.ariede@gmail.com",
    url="http://github.com/caioariede/django-location-field",
    license="MIT",
    zip_safe=False,
    platforms=["any"],
    packages=find_packages(),
    package_data={
        "location_field": [
            "static/location_field/js/*",
            "templates/location_field/*",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    include_package_data=True,
    tests_require=[
        "six",
        "pyquery<1.4",
    ],
    test_suite="runtests.runtests",
)
