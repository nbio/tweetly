# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Django settings for google-app-engine-django project.

import os
import logging
import re

# there should be a (non-svn) file named "hostname.py" in the app directory with this line:
# HOSTNAME = 'example.local'

HOST_SUFFIX = ''
try:
    from hostname import *
    HOST_SUFFIX = '.' + HOSTNAME
except:
    pass

# automatically be in debug mode in devel
DEV_ENVIRONMENT = HOST_SUFFIX != ''
DEBUG = DEV_ENVIRONMENT
TEMPLATE_DEBUG = DEBUG

PRODUCT_NAME = 'Tweetly'
DOMAIN_NAME = 'tweet.ly'
DEFAULT_TITLE = PRODUCT_NAME + ', never read the same tweet twice'
PRODUCT_EMAIL = 'ping@' + DOMAIN_NAME
COMPANY_NAME = 'nb.io'
COMPANY_URL = 'http://nb.io/'

GOOGLE_ANALYTICS_ID = 'UA-3336530-8' #TODO: add analytics!

ADMINS = (
    ('Tweetly Admin', 'info@' + DOMAIN_NAME),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'appengine'  # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
# USE_I18N = True
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/_s/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bitchesandblunts'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'nbio.django.middleware.CanonicalMiddleware',
    'nbio.django.appengine.AuthMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'

ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'nbio.django.context_processors.settings',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'appenginepatch',
    'nbio.django',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
)

# custom settings

HOSTS = {
    'app': DOMAIN_NAME + HOST_SUFFIX,
    'static': 's.' + DOMAIN_NAME + HOST_SUFFIX,
}

HOST_FILTERS = (
    re.compile(r'^localhost\d*$'),
    re.compile(r'\.latest\.tweet-ly\.appspot\.com$'),
)


AUTH_USER_MODULE = 'tweetly.models'

ALLOWED_USERS = (
    # developers
    'shaderlab@gmail.com',
    'eric.case@gmail.com',
    'cameron.walters@gmail.com',
    
    # friends
    'mathowie@gmail.com',
    'kellan@gmail.com',
    'eliana.sur@gmail.com',
    'waxpancake@gmail.com',
    'chrisw@gmail.com',
    'caterina@gmail.com',
    'merlinmann@gmail.com',
    'mcurtis@gmail.com',
)


# hella custom settings

OSD_CONTENT_TYPE = 'application/opensearchdescription+xml'
