#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains my solution to Lecture 5 Exercise 3. Lecture 5 Exercise 3 is split into two parts.
The first function always returns 10 given the parameters 9 to 21, which is deterministic.
The second function randomly returns an even number between 9 and 21, which is stochastic.

Created on Tue Nov 13 22:31:03 2018

@author: owsorber
"""

""" PART 1 """
import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10


""" PART 2 """
import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randint(5, 10) * 2
