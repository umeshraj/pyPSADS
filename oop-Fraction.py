# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 21:34:40 2015

@author: umesh
"""
def gcd(m,n):
    """ function to find the greatest common divisor"""
    if m%n == 0:
        return n
    else:
        rem = m%n
        return(gcd(n,rem))

class Fraction:
    def __init__ (self, top, bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print ("%d/%d") %(self.num, self.den)
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
        
    def __add__(self, newFrac): 
        """ overloading the + operator """
        #a/b + c/d = ad+bc/bd
        top = self.num * newFrac.den + newFrac.num*self.den
        bot = self.den*newFrac.den
        gcdNum = gcd(top, bot)
        resFrac = Fraction(top/gcdNum, bot/gcdNum)        
        return(resFrac)
        
    def __eq__(self, newFrac):
        """ adding deep equality"""
        #a/b = c/d implies ad = bc
        left = self.num * newFrac.den
        right = self.den * newFrac.num
        return(left == right)

myF1 = Fraction(3,5)
myF2 = Fraction(4,5)
myF3 = myF1 + myF2
myF4 = Fraction(6,10)

print(myF3) #test addition
print(myF1 == myF4)