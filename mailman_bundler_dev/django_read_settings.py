#!/usr/bin/env python
# Copyright (C) 2009-2014 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <http://www.gnu.org/licenses/>.

"""
This module/scripts allows printing values from a Django settings file.

It supports getting keys, and gettings subvalues of keys using
``key.subkey1.subkey2`` when the value of ``key`` is a dictionnary.
"""

from __future__ import print_function

import sys
from optparse import OptionParser
from django.conf import settings


def get_value(settings, key):
    """
    >>> from collections import namedtuple
    >>> s = namedtuple("Settings", ["foo"])
    >>> s.foo = "bar"
    >>> get_value(s, "foo")
    bar
    >>> s.foodict = {"subkey": "subvalue"}
    >>> get_value(s, "foodict.subkey")
    subvalue
    >>> s.foodict2 = {"subkey1": {"subkey2": "subvalue"}}
    >>> get_value(s, "foodict2.subkey1.subkey2")
    subvalue
    >>> get_value(s, "absent")
    Traceback (most recent call last):
        ...
    AttributeError: type object 'Settings' has no attribute 'absent'
    >>> get_value(s, "foodict.absent")
    Traceback (most recent call last):
        ...
    KeyError: 'absent'
    """
    value = settings
    for k in key.split("."):
        if isinstance(value, dict):
            value = value[k]
        else:
            value = getattr(value, k)
    return value


def main():
    parser = OptionParser(usage="%prog [KEY1] [KEY2] [...]")
    #parser.add_option("-d", "--debug", action="store_true")
    opts, args = parser.parse_args()
    if not args:
        print("\n".join(k for k in dir(settings) if not k.startswith("__")))
    for key in args:
        try:
            print(get_value(settings, key))
        except (KeyError, AttributeError) as e:
            print("No such value: {0}".format(e), file=sys.stderr)

if __name__ == "__main__":
    main()
