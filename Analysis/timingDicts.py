# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 08:12:40 2015

@author: umesh
"""

from timeit import Timer
import random

#listTimer = Timer("randNum in x","from __main__ import x, randNum")
print ("%10s %10s %10s") %('Size', 'list(ms)', 'dict(ms)')  
for i in range(10000,100001,20000):    
    # the rand function goes inside so we search for a new number each time    
    commonTimer = Timer("random.randrange(%d) in x" %i,\
    "from __main__ import random, x")  
 
    x = list(range(i))
    listTime = commonTimer.timeit(number=1000)
    
    x = {j:None for j in range(i)}
    dictTime = commonTimer.timeit(number=1000)
    print ("%10d %10f %10f") %(i, listTime, dictTime)    
    