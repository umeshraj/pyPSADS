# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 07:51:50 2015

@author: umesh
"""

from timeit import Timer

popZeroTimer = Timer("x.pop(0)","from __main__ import x")
popEndTimer = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
popZeroAns = popZeroTimer.timeit(number=1000)
print "pop(0) takes %f s" %popZeroAns

x = list(range(2000000))
popEndAns = popEndTimer.timeit(number=1000)
print "pop() takes %f s" %popEndAns

# Loop these timers over multiple values of x

print("%15s %15s") %("pop(0)", "pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    popZeroAns = popZeroTimer.timeit(number=1000)    
    x = list(range(i))
    popEndAns = popEndTimer.timeit(number=1000)

    print("%15.5f %15.5f") %(popZeroAns, popEndAns)