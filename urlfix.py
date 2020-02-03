#!/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib.parse
import pyperclip

#if len(sys.argv)==1:
def usage():
	print ("Usage: %s <url>" % sys.argv[0][sys.argv[0].rfind('/')+1:])
#	sys.exit(-1)

#url = sys.argv[1]
url = pyperclip.paste()
#fixedurl = urllib.unquote(url)  # in python version prior to 3.6
fixedurl = urllib.parse.unquote(url)
print(fixedurl)
pyperclip.copy(fixedurl)

