#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL = ''
THEME = 'Flex'
PATH = 'content'

AUTHOR = 'Charles Brunet'
SITENAME = 'Charles Brunet'
SITETITLE = 'Charles Brunet'
SITESUBTITLE = 'Le site'
SITEDESCRIPTION = 'Le site de Charles Brunet website'
SITELOGO = SITEURL + "/images/cbrunet.jpg"
# FAVICON

BROWSER_COLOR = "#33300"
ROBOTS = "index, follow"

# COPYRIGHT_NAME = "moi"
COPYRIGHT_YEAR = "Hier, aujourd'hui et demain"

MAIN_MENU = True
DISABLE_URL_HASH = True

STATIC_PATHS = ["extra/cbrunet.css"]
EXTRA_PATH_METADATA = {
    "extra/cbrunet.css": {"path": "static/cbrunet.css"},
}
CUSTOM_CSS = "static/cbrunet.css"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

USE_FOLDER_AS_CATEGORY = True


TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'fr'
OG_LOCALE = 'fr_CA'
LOCALE = ('fr_CA', 'fr_CA.utf8')
I18N_TEMPLATES_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          )

# Social widget
SOCIAL = (
    ('github', 'https://github.com/cbrunet'),
    ('stack-overflow', 'https://stackoverflow.com/users/621944/charles-brunet'),
    ('linkedin', 'https://www.linkedin.com/in/charlesbrunet/'),
)

MENUITEMS = (
    ("Mariage", "/pages/mariage.html"),
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_DATE = 'fs'
DEFAULT_PAGINATION = 10
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True