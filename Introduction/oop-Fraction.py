# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 21:34:40 2015
Making a Fraction class: https://goo.gl/YJ5Sjw
@author: umesh
"""

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def show(self):
        print("{0}/{1}".format(self.num, self.den))

    def __str__(self):
        out_str = "{0}/{1}".format(self.num, self.den)
        return out_str

myFrac = Fraction(3, 4)
myFrac.show()
print("I ate {0} of my pizza".format(myFrac))

