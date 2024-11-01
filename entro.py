#!/usr/bin/env python3
# ruff: noqa: T201

import sys
from math import log

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0][sys.argv[0].rfind('/') + 1:]} <n1> <n2> ...")
    sys.exit(-1)

if len(sys.argv) == 2:
    # sys.argv.append(f"{1-eval(sys.argv[1])}")
    if sys.argv[1].find("/") > 0:
        num, den = map(float, sys.argv[1].split("/"))
        sys.argv.append(f"{den-num:g}/{den:g}")
    else:
        sys.argv[1] = f"{eval(sys.argv[1]):g}"
        sys.argv.append(f"{1-eval(sys.argv[1])}")


print(f"Probabilities include {', '.join(sys.argv[1:])}")

entropy = 0.0
summation = 0
for item in sys.argv[1:]:
    ni = eval(item)
    if ni != 0:
        entropy += -ni * log(ni, 2)
    summation += ni
entropy = entropy / summation + log(summation, 2)

print(f"entropy is: {entropy}")
