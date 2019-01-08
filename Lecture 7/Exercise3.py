#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains my solution to Lecture 7 Exercise 3.
The following method takes in a list of strings and computes the standard deviation of their
lengths.

Created on Tue Jan 8 08:23:40 2019

@author: owsorber
"""

def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')
    
    sumOfLengths = 0
    for string in L:
        sumOfLengths += len(string)
    
    mean = sumOfLengths / len(L)
    
    tot = 0.0
    for string in L:
        tot += (len(string) - mean) ** 2
    
    return (tot / len(L)) ** 0.5

# TESTING method (Not part of solution to exercise)
print(stdDevOfLengths(['a', 'z', 'p']))
print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
