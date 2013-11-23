# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath(''))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Recommender Systems'
copyright = u'2013, Eko Indarto'
version = '0.7'
release = '0.7.5'
exclude_patterns = ['_build']
add_function_parentheses = True
add_module_names = False
pygments_style = 'sphinx'
autoclass_content = 'both'

# -- Options for HTML output ----------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]

html_static_path = ['_static']
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
htmlhelp_basename = 'Recommender Systems'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
'papersize': 'a4paper',
'pointsize': '10pt',
}

latex_documents = [
  ('index', 'Recommender Systems.tex', u'Recommender Systems Documentation',
   u'Eko Indarto', 'manual'),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    ('index', 'Recommender Systems', u'Recommender Systems Documentation',
     [u'Eko Indarto'], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
  ('index', 'Recommender Systems', u'Recommender Systems Documentation',
   u'Eko Indarto', 'Recommender Systems', 'One line description of project_name.',
   'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

epub_title = u'Recommender Systems'
epub_author = u'Eko Indarto'
epub_publisher = u'Eko Indarto'
epub_copyright = u'2013, Eko Indarto'
epub_basename = u'Recommender Systems'
epub_theme = 'epub'
epub_show_urls = 'footnote'
epub_use_index = True
