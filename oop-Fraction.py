# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 21:34:40 2015

@author: umesh
"""

class Fraction:
    def __init__ (self, top, bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print ("%d/%d") %(self.num, self.den)
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
        
    def __add__(self, newFrac): 
        #a/b + c/d = ad+bc/bd
        top = self.num * newFrac.den + newFrac.num*self.den
        bot = self.den*newFrac.den
        resFrac = Fraction(top,bot)
        return(resFrac)
        
    def gcd(m,n):
        if m%n == 0:
            return n
        else:
            rem = m%n
            return(gcd(n,rem))
            

myF1 = Fraction(3,5)
myF2 = Fraction(4,5)
myF3 = myF1 + myF2
print(myF3)