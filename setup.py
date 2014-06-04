import re
import sys

from setuptools import setup

if sys.hexversion < 0x20700f0:
    print 'Mailman requires at least Python 2.7'
    sys.exit(1)


setup(
    name            = 'mailman-bundler-dev',
    version         = '1',
    description     = 'Mailman with its admin and archiving interfaces(development version)',
    long_description= """\
This is GNU Mailman, a mailing list management system distributed under the
terms of the GNU General Public License (GPL) version 3 or later.
This package installs GNU Mailman alongside its administration and archiving
interfaces, Postorius and HyperKitty.
""",
    author          = 'The Mailman Developers',
    author_email    = 'mailman-developers@python.org',
    license         = 'GPLv3',
    url             = 'http://www.list.org',
    keywords        = 'email',
    #packages        = ['mailman_bundler'],
    #include_package_data = True,
    install_requires = [
        "zc.buildout"
        ],
    entry_points = {
        "console_scripts": [
            "django-read-settings = mailman_bundler_dev.django_read_settings:main",
            ],
        },
    )
