# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 20:36:35 2015

@author: umesh
"""

def recListSum(inList):
    if len(inList) == 1:
        return inList[0]
    else:
        return inList[0] + recListSum(inList[1:])
    
tmpList = range(1,11)
print(recListSum(tmpList))