#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ***** BEGIN GPL LICENSE BLOCK *****
#
# Copyright (C) 2018: S.M.J.R.,
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# ***** END GPL LICENCE BLOCK *****
# Change Logs:
# Tue 22 May 2018 04:50:34 AM +0430
# ver 0.01: Initial version

__author__ = "S.M.J.R."
__version__ = 0.1
__date__ = "22May2018"
__email__ = 'javadr@gmail.com'

import sys, os
from itertools import permutations, combinations
from subprocess import call

def choose(chars, k):
    for item in combinations(chars, k): makewords(item)

def makewords(chars):
    for item in permutations(chars): 
#        count = call("grep {0} Bwords.txt -cxq".format(''.join(item)), stdout=None, shell=True)
#        if count !=0: print(''.join(item), count)
        w = ''.join(item)
        if w in worddic: print(w)
        
        
def usage():
    print ("""Word Maker ver {0}[{1}]
    Usage:
    \t{2} <char1> <char2> k""".format(__version__, __date__, sys.argv[0]))

if __name__ == '__main__':
    chars = sys.argv[1:-1] if len(sys.argv) > 4 else sys.stdin.readlines()
    k = int(sys.argv[-1])
    if not chars:#len(sys.argv) < 2 and len(linesinput)==0:
        usage()
        sys.exit()
        
    curdir = os.path.dirname(os.path.realpath(__file__)) 
    worddic = {i:1 for i in open("{0}/Bwords.txt".format(curdir)).read().split()}        
#    print(worddic)

    choose(chars, k)        
