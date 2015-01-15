# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 08:30:59 2015

@author: umesh
"""

from pythonds.basic import Stack


def dec2bin(dec):
    base = 2
    quotient = dec
    s = Stack()  # to store remainders
    while quotient >= base:
        rem = quotient % base
        quotient = quotient//base
        s.push(rem)
    s.push(quotient)

    binStr = ''
    while not s.isEmpty():
        binStr = binStr + str(s.pop())

    return binStr


print dec2bin(2)
