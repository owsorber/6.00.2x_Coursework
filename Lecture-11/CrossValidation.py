#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file explores cross-validation, a way of testing the validity of a model by cross-checking
it with new data. In the file, I generate noisy parabolic data, but given the nature of higher
degree polynomials, regressions of higher-degree polynomials yield higher r^2 values because
there are more coefficients that can be tuned to match the data's variability. However, if we
were modeling a real-world phenomenon, we would want to know that the data is indeed parabolic.
To employ cross-validation, we generate two data sets, and the crossValidation function 
computes the r-squared of a dataset's polynomial regression when compared to the other dataset.
After doing this, the 2nd degree quadratic regressions yield the best r^2 value because it is
the best fit.
Code inspired by Lecture 11 of MIT Course 6.00.2x

Created on Tue Apr 2 16:41:38 2019

@author: owsorber
"""

import random
import pylab
import numpy

# Returns a tuple of x and y values by computing the y values using quadratic's coefficients
def genNoisyParabolicData(a, b, c, xVals):
    yVals = []
    for x in xVals:
        theoreticalVal = a*x**2 + b*x  + c
        yVals.append(theoreticalVal + random.gauss(0, 35))
    return (xVals, yVals)

def rSquared(observed, predicted):
    error = 0
    for i in range(len(observed)):
        error += (observed[i] - predicted[i]) ** 2
    return 1 - error / (numpy.var(observed) * len(observed)) # multiply by length to simply get sum of squares


# This function plots several polynomial fits (models) along with the original data
# parameters: data (tuple of x values, y values) and models (list of polynomial fits)
def plotPolynomialFit(data, models):
    xVals = pylab.array(data[0])
    yVals = pylab.array(data[1])
    pylab.plot(xVals, yVals, 'bo', label="Noisy Parabolic Data")
    
    fitcols = ["b", "r", "g", "k"]
    
    modelnum = 0
    for model in models:
        degree = len(model) - 1
        estYVals = pylab.polyval(model, xVals) # generate array of estimated y values
        pylab.plot(xVals, estYVals, fitcols[modelnum], label="Degree " + str(degree) + ", r^2 = "\
                   + str(crossValidation(model, (xVals, yVals))))
        modelnum += 1
    
    pylab.legend()

# returns r-squared of model when applied to new data
def crossValidation(model, newData):
    newDataXVals = newData[0]
    newDataYVals = newData[1]
    modelYVals = pylab.polyval(model, newDataXVals)
    
    return round(rSquared(newDataYVals, modelYVals), 3)


xVals = [num for num in range(-10, 11)]
a, b, c = 3, 0, 0
degrees = (2, 4, 8, 16)

data1 = genNoisyParabolicData(a, b, c, xVals)
data2 = genNoisyParabolicData(a, b, c, xVals)

models1 = [pylab.polyfit(data1[0], data1[1], degree) for degree in degrees]
models2 = [pylab.polyfit(data2[0], data2[1], degree) for degree in degrees]

pylab.figure("21")
pylab.title("Noisy Parabolic Data 2 with Models from Data 1")
plotPolynomialFit(data2, models1)

pylab.figure("12")
pylab.title("Noisy Parabolic Data 1 with Models from Data 2")
plotPolynomialFit(data1, models2)

