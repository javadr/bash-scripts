#!/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import log

if len(sys.argv) < 3:
    print("Usage: %s <n1> <n2> ..." % sys.argv[0][sys.argv[0].rfind('/') + 1:])
    sys.exit(-1)

entropy = 0.0
isum = 0
for item in sys.argv[1:]:
    ni = eval(item)
    if ni != 0: entropy += -ni * log(ni, 2)
    isum += ni
entropy = entropy / isum + log(isum, 2)
print("entropy is: {}".format(entropy))
