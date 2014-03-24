#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vivacity Choir Webmaster'
SITENAME = u'Vivacity Choir'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

LINKS = (
    ('Vivacity Concert Tickets', 'http://vivacitychoir.ticketsource.co.uk/'),
    ('Vivacity YouTube Page', 'http://www.youtube.com/user/vivacitychoir/'),)

# Social widget
SOCIAL = ()
#    ('facebook', 'https://www.facebook.com/pages/Vivacity-Choir/113608155369081'),
#    ('twitter', 'https://twitter.com/vivacitychoir'),
#    ('youtube', 'http://www.youtube.com/user/vivacitychoir/'), )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "bootstrap2"

PAGE_DIR = 'pages'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

ARTICLE_DIR = 'articles'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_LANG_URL = 'articles/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{slug}-{lang}.html'

SIDEBAR_FACEBOOK_BADGE = """
<li style="text-align: center">
  <a href="http://www.facebook.com/pages/Vivacity-Choir/113608155369081"
     target="_TOP" title="Vivacity Choir">
  <img src="http://badge.facebook.com/badge/113608155369081.597.1088970148.png"
       width="" height="" style="border: 0px;" />
  </a>
</li>
"""
SIDEBAR_TICKETS_LINK = """
<li style="text-align: center">
  <a href="http://vivacitychoir.ticketsource.co.uk"
     title="Buy tickets for Vivacity Choir concerts">
    <img border="0" width="140" height="105" alt="Book now"
         src="http://www.ticketsource.co.uk/images/buyTickets/buyTickets-small.png" style="border: 1px;"/>
  </a>
</li>
"""

BANNER_IMAGE = "/images/banner.jpg"
