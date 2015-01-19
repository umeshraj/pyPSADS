# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 08:00:17 2015

@author: umesh
"""


def isPalindrome(inStr):
    if len(inStr) < 2:
        return True
    if inStr[0] != inStr[-1]:
        return False
    else:
        return isPalindrome(inStr[1:-1])


print isPalindrome("umesh")
