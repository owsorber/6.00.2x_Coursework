#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file conducts the Button-Laplace Needle Dropping Experiment to computationally estimate
the value of pi. If we imagine a circle of radius 1 inscribed within a 2 x 2 square, we know 
the area of the square is 4 and the area of the circle is π. If we randomly select points
within the square and find the proportion of randomly-selected points within the circle,
the value of the circle's area (which is the value of π) should be roughly equal to 4 times
the proportion of points within the circle. The following set of functions set up the simulation
and precisePi finds a 95% confidence interval for the value of pi to compute it within a 
precision.
Code inspired by Lecture 8 of MIT Course 6.00.2x

Created on Sat Feb 9 22:16:42 2019

@author: owsorber
"""

import random

# Helper function for getting mean and standard deviation of pi estimates
def getMeanAndStd(sample):
    mean = sum(sample) / float(len(sample))
    tot = 0.0
    for x in sample:
        tot += (x - mean) ** 2
    stdev = (tot/len(sample)) ** 0.5
    return mean, stdev

# Compute the proportion of needles landing in circle and return the estimated value of pi 
def throwNeedles(numNeedles):
    inCircle = 0 # number of needles landed within circle
    for needle in range(numNeedles):
        x = random.random()
        y = random.random()
        distFromOrigin = (x*x + y*y) ** 0.5 # distance formula
        if distFromOrigin <= 1.0: # if needle is within 1 unit of origin, it is within circle
            inCircle += 1
    return 4 * (inCircle/float(numNeedles))

# Return the mean and standard deviation of sample means to estimate pi
def getPiEstimate(numNeedles, numTrials):
    estimates = []
    for i in range(numTrials):
        estimates.append(throwNeedles(numNeedles))
    result = getMeanAndStd(estimates)
    print("For", numNeedles, "needles with", numTrials, "trials, mean =", result[0], "stdev =", result[1])
    return result

# Find a 95% confidence interval for the value of pi of where pi = estimate +- precision
def precisePi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev * 2 >= precision: # compare sDev * 2 because z = 2 produces 95% confidence interval
        currEst, sDev = getPiEstimate(numNeedles, numTrials)
        numNeedles *= 2
    return currEst

precisePi(0.01, 1000)
print("DONE")
