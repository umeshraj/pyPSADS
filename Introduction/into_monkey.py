# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 07:59:11 2015
https://goo.gl/WPqpse
@author: umesh
"""

#function to simulate monkeys writing shakespeare
#make a random string  “this is a test of abcd”

import string
import random

def mkRandomStr(str_len):
    """ make a random string of length str_len"""
    out = ""
    alphas = string.ascii_lowercase + ' '
    alphas_len = len(alphas)
    for idx in range(str_len):
        rand_idx = random.randint(0, alphas_len-1)
        out = out + alphas[rand_idx]
    return out

def score(goalStr, testStr):
    """ compute the similarity between goalStr and testStr"""
    score = 0
    for idx in range(len(goalStr)):
        if goalStr[idx] == testStr[idx]:
            score += 1
    score = score/len(goalStr)
    return score

