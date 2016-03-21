"""
File to easily switch between configurations between production and
development, etc.
"""

import os


# You must set each of these in your heroku environment with the heroku
# config:set command. See README.md for more information.
HEROKU_ENV_REQUIREMENTS = ('HEROKU', 'SECRET_KEY', 'GITHUB_CLIENT_ID',
                           'GITHUB_SECRET', 'REPO_OWNER', 'REPO_NAME',
                           'REPO_OWNER_ACCESS_TOKEN', 'REDISCLOUD_URL',
                           'REDIS_URL', 'MAILCHIMP_API_KEY',
                           'MAILCHIMP_LIST_ID', 'MAILCHIMP_STACKS_GROUP_NAME',
                           'SECONDARY_REPO_OWNER', 'SECONDARY_REPO_NAME',
                           'BASE_URL', 'CELERY_BROKER_URL',
                           'CELERY_TASK_SERIALIZER', 'HOSTING_SUBDIRECTORY')


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    HEROKU = False
    SECRET_KEY = 'not-a-good-value'

    # Details of the repo where all articles are stored.  The GITHUB_CLIENT_ID
    # and GITHUB_SECRET should allow full-access to this database.
    GITHUB_CLIENT_ID = 'replace-me'
    GITHUB_SECRET = 'replace-me'
    REPO_OWNER = None
    REPO_NAME = None
    REPO_OWNER_ACCESS_TOKEN = None

    CELERY_TASK_SERIALIZER = 'json'
    CELERY_BROKER_URL = None

    # Secondary (optional) repo for articles that are not editable
    SECONDARY_REPO_OWNER = None
    SECONDARY_REPO_NAME = None

    # For caching
    REDISCLOUD_URL = None

    # For celery
    REDIS_URL = None

    MAILCHIMP_API_KEY = None
    MAILCHIMP_LIST_ID = None
    MAILCHIMP_STACKS_GROUP_NAME = None

    BASE_URL = ''

    # Set this to something like '/guides' if your hosting this application on
    # a subdirectory with a proxy pass rule that sends all /guides/* requests
    # to this app.  Thus, this app responds to '/guides' with the '/' rule.
    HOSTING_SUBDIRECTORY = ''


class DevelopmentConfig(Config):
    DEBUG = True
