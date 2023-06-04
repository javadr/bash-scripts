#!/usr/bin/env python3

import sys
from math import log

if len(sys.argv) < 2:
    print("Usage: %s <n1> <n2> ..." % sys.argv[0][sys.argv[0].rfind('/') + 1:])
    sys.exit(-1)

if len(sys.argv) == 2:
    sys.argv.append(f"{1-eval(sys.argv[1])}")

entropy = 0.0
isum = 0
for item in sys.argv[1:]:
    ni = eval(item)
    if ni != 0: entropy += -ni * log(ni, 2)
    isum += ni
entropy = entropy / isum + log(isum, 2)
print("entropy is: {}".format(entropy))
