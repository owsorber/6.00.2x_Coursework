#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains my solution to Lecture 5 Exercise 2.

Lecture 5 Segment 1 explores stochastic processes, so the task was to simply complete the genEven()
function so that it uses the random module to return a random even number from 0 to 100 (not including 100).

Created on Tue Nov 13 22:23:00 2018

@author: owsorber
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randint(0, 49) * 2
    

# TEST for loop (Not part of solution to exercise)
for i in range(0, 100):
    print(genEven())
