# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 07:58:13 2015

@author: umesh
"""


def revString(inStr):
    if len(inStr) == 1:
        return inStr
    else:
        return revString(inStr[1:]) + inStr[0]
        
print revString("this is a test")        