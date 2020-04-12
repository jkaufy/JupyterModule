# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append("/Scripts")
sys.path.append("/Users/jkaufy/Desktop/Pydocs/sphinx/imgs")

extensions = [
             'nbsphinx',
             'sphinx.ext.autodoc',
              'jupyter_sphinx.execute',
             ]

templates_path = ['_templates']

master_doc = 'index'
source_suffix = '.rst'

# General information about the project.
project = 'CartoCosmos'
author = 'CartoCosmos Development Team'

exclude_patterns = []
highlight_language = 'python'
pygments_style = 'sphinx'

# Output file base name for HTML help builder.
html_theme = "default"
htmlhelp_basename = 'CartoCosmosDoc'
html_static_path = ['_static']
