#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the code for my Lecture 8 Project. For this project, I decided to
conduct the Button-Laplace Needle Dropping Experiment in a Monte-Carlo Simulation that
estimates the value of any integral. If we randomly select points between the 
Using the highest y-max and y-mins for height and the bounds of integration for width,
we can form a rectangle that surrounds the curve of the function. If we randomly 
select points within this rectangle, some will be within the curve and others will not.
One trial in the simulation will randomly generate points and find the proportion of 
randomly-selected points surrounded by the function curve. Multiplying by the rectangle
area yields a value roughly equal to the integral. The function estimateIntegral performs
multiple trials on the integral and creates a 95% confidence interval for the value.
One downside is that the y-bounds of the rectangle must be entered manually, but I think
this is the only way we to estimate the integral with no calculus (since finding the max
of any function would require its derivative).
Created on Mon Feb 11 18:24:22 2019

@author: owsorber
"""

import math # for math functions
import scipy.integrate # for verifying integral estimates
import random # for random needle placement

# Helper function for getting mean and standard deviation of integral estimates
def getMeanAndStd(sample):
    mean = sum(sample) / float(len(sample))
    tot = 0.0
    for x in sample:
        tot += (x - mean) ** 2
    stdev = (tot/len(sample)) ** 0.5
    return mean, stdev

# Function we will be estimating integral of
def F(x):
    return math.e ** x

"""
performTrial performs one trial of integral estimation by throwing NUM_NEEDLES needles
at a coordinate plane and calculating the proportion of needles that land within a function's
curve.

func : function for integral estimation
a : lower bound of integration
b : upper bound of integration
maxYNegative : the largest negative value of the function (0 if the range is y >= 0)
maxYPositive : the largest positive value of the function (0 if the range is y <= 0)

Returns the integral estimation for that sample of needles
"""
def performTrial(func, a, b, maxYNegative, maxYPositive):
    NUM_NEEDLES = 1000000
    withinCurvePositive = 0
    withinCurveNegative = 0
    rectArea = (b - a) * (maxYPositive - maxYNegative)
    for needle in range(NUM_NEEDLES):
        x = a + random.random() * (b - a)
        y = maxYNegative + random.random() * (maxYPositive - maxYNegative)
        if y > 0 and y < func(x):
            withinCurvePositive += 1
        elif y < 0 and y > func(x):
            withinCurveNegative += 1
            
    
    return rectArea * ((withinCurvePositive - withinCurveNegative) / float(NUM_NEEDLES))


"""
estimateIntegral estimates the integral of func from a to b by providing the mean of
sample means along with a 95% confidence interval.

func : function for integral estimation
a : lower bound of integration
b : upper bound of integration
maxYNegative : the largest negative value of the function (0 if the range is y >= 0)
maxYPositive : the largest positive value of the function (0 if the range is y <= 0)

Returns the estimated integral and prints both the estimation and actual value
"""
def estimateIntegral(func, a, b, maxYNegative, maxYPositive):
    estimates = []
    for i in range(20):
        print("Trial " + str(i + 1) + " done")
        estimates.append(performTrial(func, a, b, maxYNegative, maxYPositive))
    result = getMeanAndStd(estimates)
    
    # For 95% confidence interval
    lowerBoundEstimate = result[0] - 2*result[1]
    upperBoundEstimate = result[0] + 2*result[1]
    
    # Print estimate and actual
    print("Estimation --", "Mean =", result[0], "Between", lowerBoundEstimate, "and", upperBoundEstimate)
    print("Actual -- ", round(scipy.integrate.quad(func, a, b)[0], 10))
    
    return result


estimateIntegral(F, 0, 2, 0, math.e ** 2)

