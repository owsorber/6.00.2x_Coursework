#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains my solution to Lecture 9 Exercise 2.
The loadFile() function opens a julytemps.txt file that has a table of high and
low temperatures in July in Boston. I had to add a condition to capture non-data
lines so that they would not be interpreted. I then used pylab to create a plot
that would plot the difference in high/low temperatures for each day.
Created on Sat Mar 9 20:25:42 2019

@author: owsorber
"""

import pylab
import numpy

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    diffTemps = list(numpy.array(high) - numpy.array(low))
    pylab.plot(range(1, 32), diffTemps)
    return (low, high)
    
    
    
