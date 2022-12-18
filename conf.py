
# -- Project information -----------------------------------------------------
project = 'resume'
# copyright = '2022, Alex Haw'
author = 'Alexander Haw'

# -- General configuration ---------------------------------------------------
html_title = "Alexander Haw"
html_logo = "_images/me_full_small.png"
# html_favicon = "path/to/favicon.ico"

extensions = [
    'sphinxcontrib.images'
]

templates_path = ['_templates']
root_doc = 'input'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinxdoc'
# html_theme = 'sphinx_theme_pd'
# html_theme_path = [sphinx_theme_pd.get_html_theme_path()]
html_static_path = ['_static']