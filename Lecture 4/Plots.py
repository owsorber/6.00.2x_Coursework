#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file follows Lecture 4 Segments 1-3, which explore the Pylab library. Pylab allows data visualization by
plotting two related lists on a coordinate grid. The following code uses pylab to plot a linear (y=x),
quadratic (y=x^2), cubic (y=x^3), and exponential (y=1.4^x) function on a pair of x and y axes.

Created on Mon Nov 12 12:11:12 2018

@author: owsorber
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.4 ** i)
    
""" 
The following functions plot graphs for each relationship (linear, quadratic, cubic, exponential).
Calling them in an iPython console displays the graph in the console.
Calling them in a Python console will create a separate customizable window to view the graph.
"""

plt.figure("lin") # keyword that represents the linear graph and can be called to make changes to it
plt.title("Linear") # plot title
plt.xlabel("Sample X Points") # x-axis label
plt.ylabel("Linear f(x)") # y-axis label
plt.plot(mySamples, myLinear) # create the plot

plt.figure("quad")
plt.title("Quadratic")
plt.xlabel("Sample X Points")
plt.ylabel("Quadratic f(x)")
plt.plot(mySamples, myQuadratic)

plt.figure("cube")
plt.title("Cubic")
plt.xlabel("Sample X Points")
plt.ylabel("Cubic f(x)")
plt.plot(mySamples, myCubic)

plt.figure("expo")
plt.title("Exponential")
plt.xlabel("Sample X Points")
plt.ylabel("Exponential f(x)")
plt.plot(mySamples, myExponential)


