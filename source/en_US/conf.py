# -*- coding: utf-8 -*-
#
# Armadito documentation build configuration file, created by
# sphinx-quickstart on Tue Apr 12 17:35:15 2016.

import sys
import os

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'armaditoav-en'
copyright = u'2016, Teclib'
author = u'Teclib'
version = u'1.0'
release = version
exclude_patterns = []
pygments_style = 'sphinx'


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
htmlhelp_basename = 'armaditoavendoc'

latex_elements = {
}

latex_documents = [
    (master_doc, 'armaditoav-en.tex', u'Armadito Antivirus Documentation',
     u'Teclib', 'manual'),
]

man_pages = [
    (master_doc, 'armadito', u'Armadito Antivirus Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Armadito Antivirus', u'Armadito Antivirus Documentation',
     author, 'Armadito Antivirus', 'Armadito AV is an open-source antivirus',
     'Miscellaneous'),
]
