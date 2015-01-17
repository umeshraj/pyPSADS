# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 07:44:03 2015

@author: umesh
"""

from pythonds.basic import Stack

def baseConverter(dec, base):
    charList = '0123456789ABCDEF' #characters for base conversion
    
    s = Stack()
    while dec > 0:
        rem = dec%base
        dec = dec//base        
        s.push(rem)

    outStr = ''        
    while not s.isEmpty():
        curNum = s.pop()
        outStr += charList[curNum]
        
    return outStr
    
    
print(baseConverter(25,2))
print(baseConverter(25,16))        
        