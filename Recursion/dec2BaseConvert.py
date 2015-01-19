# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 20:49:21 2015

@author: umesh
"""


def toStr(num, base):
    """ function to convert any number to a base. O/p is a string"""
    chStr = "0123456789ABCDEF"
    if num < base:
        return chStr[num]
    else:
        return toStr(num//base, base) + chStr[num%base]

print(toStr(1453,16))
