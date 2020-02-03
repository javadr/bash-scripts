#!/bin/python
# -*- coding: utf-8 -*-

import os

for name in os.listdir('.'):
#	print name
	if os.path.isfile(name):
		try: 
			if name.decode('utf-8').encode('latin-1') != name:
				newName = name.decode('utf-8').encode('latin-1')
				os.rename(name, newName)
				print "%s file name renamed to this new one: %s" % (name, newName)
		except: pass
