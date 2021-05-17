#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018-2021: S.M.J.R.,
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# Change Logs:
# Mon 17 May 2021 02:32:55 PM +0430
# ver 0.11: simplification of code 
# Tue 22 May 2018 04:50:34 AM +0430
# ver 0.01: Initial version

__version__ = 0.11
__date__ = "17May2021"

import sys
from itertools import permutations, combinations
from pathlib import Path


def choose(chars, k):
    finalwords = set()
    for item in combinations(chars, k):
        finalwords.update(makewords(item))
    return finalwords
    
def makewords(chars):
    words = set( ''.join(item) for item in permutations(chars) if ''.join(item) in worddic )
    return words

def usage():
    print(f"""Word Maker ver {__version__} [{__date__}]
    Usage:
    \t{Path(sys.argv[0]).name} <char1> <char2> .... <charN> k  \t # k <= N""")

if __name__ == '__main__':
    chars = sys.argv[1:-1]
    try: 
        k = int(sys.argv[-1])
    except ValueError: 
        usage()
        sys.exit()

    if not chars:  #len(sys.argv) < 2
        usage()
        sys.exit()
    
    # os.path.dirname(os.path.realpath(__file__))
    curdir = Path(sys.argv[0]).parent.absolute()
    worddic = {i: 1 for i in open(f"{curdir}/Bwords.txt").read().split()}

    print('\n'.join(choose(chars, k)))
