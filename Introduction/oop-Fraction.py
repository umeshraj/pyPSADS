# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 21:34:40 2015
Making a Fraction class: https://goo.gl/YJ5Sjw
@author: umesh
"""


def gcd(m, n):
    """ greatest common divisor of two positive integers"""
    while (m%n !=0):
        m, n = n, m%n
    return n

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def show(self):
        print("{0}/{1}".format(self.num, self.den))

    def __str__(self):
        out_str = "{0}/{1}".format(self.num, self.den)
        return out_str

    def __add__(self, new_frac):
        new_num = self.num*new_frac.den + self.den*new_frac.num
        new_den = self.den * new_frac.den
        return Fraction(new_num, new_den)

# testing the show/print functions
myFrac = Fraction(3, 4)
myFrac.show()
print("I ate {0} of my pizza".format(myFrac))

# adding fractions
f1=Fraction(1,4)
f2=Fraction(1,2)
f3=f1+f2
print(f3)
