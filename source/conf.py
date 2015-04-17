# -*- coding: utf-8 -*-
#
# Minimum neccessary conf options for LaTeX output.
# Replaces sphinx-quickstart generated conf.py.
#

import sys
import os

# -- General configuration ------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'Document Title'
copyright = u'years, Author Name'

version = '0.0'
release = version

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
'papersize': 'letterpaper',

'pointsize': '11pt',

'fontpkg': '\\usepackage[defaultsans]{droidsans}\n\\renewcommand*\\familydefault{\\sfdefault}',

'fncychap': '',

'preamble': '\\usepackage{strat}',
}

latex_documents = [
  ('index', 'output_file.tex', '', u'Author Name', 'howto'),
]

latex_additional_files = ['strat.sty']
