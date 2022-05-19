# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Benchmark 8760 Platform'
copyright = '2022, JBB'
author = 'JBB'

release = '1.0'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'bizstyle'
html_logo = 'JBB-Icon-r4-short.png'

html_static_path = ['_static']

html_css_files = [
    'benchmark8760.css'
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
