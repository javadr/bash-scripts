#!/bin/env python3
"""
URL Unicode Converter

This program is designed to convert a URL with Unicode characters into its unicode decoded form
when it was copied from browser's address bar. It can be useful when working with URLs that contain
non-ASCII characters and need to be converted back to Unicode for various purposes.

Usage:

    1. Copy a URL with Unicode characters from the browser's address bar.
    2. Run this program.
    3. The program will automatically decode the URL into Unicode and
    store it back into the clipboard.

Please note that this program assumes the presence of `pyperclip` module and
requires it for proper functionality.

Disclaimer: This program is provided as-is without any warranties. Use it at your own risk.
"""

import argparse
import urllib.parse
import pyperclip


parser = argparse.ArgumentParser(description='Process the clipboard\'s text.')
parser.add_argument('-u', dest='urlfix_or_newline', action='store_true', default=True)
parser.add_argument('-n', dest='urlfix_or_newline', action='store_false', )
args = parser.parse_args()

output = pyperclip.paste()

if args.urlfix_or_newline:  # urlfix
    output = urllib.parse.unquote(output)
#    output = urllib.unquote(output)  # in python version prior to 3.6
else:  # newline remove
    output = output.replace('\n\n', '!$@#').replace('\n',
                                                    ' ').replace('!$@#', '\n').title()
pyperclip.copy(f"{output}")
print(output)
