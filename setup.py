"""Sphinx Bootstrap Theme package."""
from setuptools import setup

from pandas_sphinx_theme import __version__


setup(
    name="pandas-sphinx-theme",
    version=__version__,
    description="Sphinx Bootstrap Theme - pandas version.",
    url="https://github.com/pandas-dev/pandas-sphinx-theme",
    #
    packages=["pandas_sphinx_theme"],
    package_data={
        "pandas_sphinx_theme": [
            "theme.conf",
            "*.html",
            "static/css/*.css",
            "static/js/*.js",
        ]
    },
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={"sphinx.html_themes": ["pandas_sphinx_theme = pandas_sphinx_theme"]},
    install_requires=["sphinx"],
)