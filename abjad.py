#!/usr/bin/python3
# -*- coding: utf-8 -*-
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
# ***** END GPL LICENCE BLOCK *****
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
__version__ = 0.12
__date__ = "9Apr2017"
__email__ = 'javadr@gmail.com'

import sys
import string


def abjadCalculate(inputStr):
    s = 0
    abjDic = {
        u"ا": 1,
        u"إ": 1,
        u"أ": 1,
        u"آ": 2,
        u"ء": 1,
        u"ؤ": 1,
        u"ئ": 1,
        u"ب": 2,
        u'پ': 2,
        u'چ': 3,  #for persian support
        u"ج": 3,
        u"د": 4,
        u"ه": 5,
        u"و": 6,
        u"ز": 7,
        u'ژ': 7,  #for persian support
        u"ح": 8,
        u"ط": 9,
        u"ي": 10,
        u"ی": 10,
        u"ك": 20,
        u"ک": 20,
        u'گ': 20,  #for persian support
        u"ل": 30,
        u"م": 40,
        u"ن": 50,
        u"س": 60,
        u"ع": 70,
        u"ف": 80,
        u"ص": 90,
        u"ق": 100,
        u"ر": 200,
        u"ش": 300,
        u"ت": 400,
        u"ة": 400,
        u"ث": 500,
        u"خ": 600,
        u"ذ": 700,
        u"ض": 800,
        u"ظ": 900,
        u"غ": 1000
    }
    for letter in inputStr:
        s += abjDic.get(letter, 0)
    return s


def usage():
    print("""Abjad Calculus ver {0}[{1}]
    Usage:
    \tabjad.py <IN1> <IN2> ....""".format(__version__, __date__))


if __name__ == '__main__':
    allwords = sys.argv[1:] if len(
        sys.argv) > 1 else sys.stdin.readline().split()
    if not allwords:  #len(sys.argv) < 2 and len(linesinput)==0:
        usage()
        sys.exit()

    abjsum = 0
    maxStrLen = max([len(i) for i in allwords])

    print("Abjad Calculus ver. {}:\n".format(__version__))
    for i, item in enumerate(allwords):
        val = abjadCalculate(item)
        abjsum += val
        print("{0} \t {1}".format(item.replace('\n', ''), val))

    print("\nsum: {}".format(abjsum))
