#!/bin/env python3

import urllib.parse
import pyperclip
import argparse

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
