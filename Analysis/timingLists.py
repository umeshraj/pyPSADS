# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 08:31:17 2015

@author: umesh
"""


def test1():
    """ grow list by concatenation """
    outList = []
    for i in range(1000):
        outList = outList + [i]


def test2():
    """ grow list by appending"""
    outList = []
    for i in range(1000):
        outList.append(i)

def test3():
    """ grow list by comperhension"""
    outList = [i for i in range(1000)]
    
    
def test4():
    """" grow a list using range"""
    outList = list(range(0, 1000))
    

## timing these tloop    
from timeit import Timer
t1 = Timer("test1()","from __main__ import test1")
print "Concatenation time %f ms" %t1.timeit(number=1000)

t2 = Timer("test2()", "from __main__ import test2")
print "Append time %f ms" %t2.timeit(number=1000)

t3 = Timer("test3()", "from  __main__ import test3")
print "Comprehension time %f ms" %t3.timeit(number=1000)

t4 = Timer("test4()", "from __main__ import test4")
print "Range time %f ms" %t4.timeit(number=1000)