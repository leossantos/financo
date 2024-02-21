"""Sphinx configuration."""

project = "Financo"
author = "Leonardo Soares Santos"
copyright = "2024, Leonardo Soares Santos"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
