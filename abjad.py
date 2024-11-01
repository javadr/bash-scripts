#!/usr/bin/env python3
# ruff: noqa: T201

# ***** BEGIN GPL LICENSE BLOCK *****
#
# Copyright (C) 2009: S.M.J.R.,
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
# ***** END GPL LICENSE BLOCK *****
# Change Logs:
# Sun 09 Apr 2017 10:15:55 AM +0430
# ver 0.12: Support for ة as ت
# Mon 21 Nov 2016 10:12:05 AM IRST
# ver 0.11: Minor bug in summation output
# Sat 23 Jul 2016 12:47:02 PM IRDT
# ver 0.1: Accept input from pipe in shell
# Mon 23 Dec 2013 13:30:52 IRST
# ver 0.01: Initial version

__author__ = "S.M.J.R."
__version__ = 0.13
__date__ = "1Nov2024"

import sys


def abjad_compute(inputStr):
    s = 0
    abjDic = {
        "ا": 1,
        "إ": 1,
        "أ": 1,
        "آ": 2,
        "ء": 1,
        "ؤ": 1,
        "ئ": 1,
        "ب": 2,
        "پ": 2,
        "چ": 3,  # for persian support
        "ج": 3,
        "د": 4,
        "ه": 5,
        "و": 6,
        "ز": 7,
        "ژ": 7,  # for persian support
        "ح": 8,
        "ط": 9,
        "ي": 10,
        "ی": 10,
        "ك": 20,
        "ک": 20,
        "گ": 20,  # for persian support
        "ل": 30,
        "م": 40,
        "ن": 50,
        "س": 60,
        "ع": 70,
        "ف": 80,
        "ص": 90,
        "ق": 100,
        "ر": 200,
        "ش": 300,
        "ت": 400,
        "ة": 400,
        "ث": 500,
        "خ": 600,
        "ذ": 700,
        "ض": 800,
        "ظ": 900,
        "غ": 1000,
    }
    for letter in inputStr:
        s += abjDic.get(letter, 0)
    return s


def usage():
    print(
        f"""Abjad Calculator ver {__version__}[{__date__}]
    Usage:
    \tabjad.py <IN1> <IN2> ....""",
    )


if __name__ == "__main__":
    all_words = sys.argv[1:] if len(sys.argv) > 1 else sys.stdin.readline().split()
    if not all_words:  # len(sys.argv) < 2 and len(linesinput)==0:
        usage()
        sys.exit()

    abjad_sum = 0
    maxStrLen = max([len(i) for i in all_words])

    print(f"Abjad Calculator ver. {__version__}:\n")
    for i, item in enumerate(all_words):
        val = abjad_compute(item)
        abjad_sum += val
        print(f"{item.replace('\n', '')} \t {val}")

    print(f"\nsum: {abjad_sum}")
