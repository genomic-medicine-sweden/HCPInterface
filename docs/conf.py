# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
from toml import load
sys.path.insert(0, os.path.abspath(".."))

pyproject = load("../pyproject.toml")
pyproject_project : dict = pyproject["project"]

project = pyproject_project["name"]
#copyright = "2024, Erik Brink"
author = ""
for author_ in pyproject_project["authors"]:
    author += (author_["name"] + ", ")
author = author[:-2]

show_authors = True
html_show_copyright = False
release = pyproject_project["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx_markdown_builder"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
