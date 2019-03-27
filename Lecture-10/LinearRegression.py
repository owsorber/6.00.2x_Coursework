#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file opens data from a spring experiment for calculating k, the spring constant.
The function fitData plots the displacement of the spring when a certain mass was hung
on the spring vs. the spring force required to counter the mass's gravitational force.
Then, the polyfit function of pylab is used to fit the data to a linear polynomial by
minimizing the sum of the square of the residuals. Finally, polyval is used to grab the
y values of the model and the linear fit is plotted, the estimated k value in the legend.
In the legend is also the Coefficient of Determination, r^2, which divides
the sum of the squares of the residuals (unexplained variation) by the sum of the squares 
of the differences between the observed value and mean observed value (total variation).
This value is then subtracted from 1 to get the proportion of variance in distance that is 
explained by force.

New pylab functions:
    polyfit: 
        - Takes in x values, y values, and polynomial degree
        - Returns a tuple of polynomial degree
    polyval:
        - Takes in a polynomial model (tuple of coefficients) and list of measured x values
        - Returns a list of y values using polynomial model

Created on Sun Mar 24 21:49:37 2019

@author: owsorber
"""

import pylab
import numpy

def getSpringData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline() # discard header
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def rSquared(observed, predicted):
    error = 0
    for i in range(len(observed)):
        error += (observed[i] - predicted[i]) ** 2
    return 1 - error / (numpy.var(observed) * len(observed)) # multiply by length to simply get sum of squares


def fitData(fileName):
    xVals, yVals = getSpringData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    
    model = pylab.polyfit(xVals, yVals, 1) # fit data to line (degree = 1)
    estYVals = pylab.polyval(model, xVals) # generate array of estimated y values
    estimatedK = round(1/model[0], 3)
    
    pylab.plot(xVals, estYVals, 'r', label = "Linear Fit, k = " + str(estimatedK)\
               + ", r^2 = " + str(round(rSquared(yVals, estYVals), 3)))
    pylab.title("Measured Displacement of Spring")
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    pylab.legend()

fitData("SpringData.txt")

