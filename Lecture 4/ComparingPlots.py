#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file follows Lecture 4 Segment 4, which explores ways to compare plots with the pylab library. The 
following code creates two plots. One compares a linear and quadratic function, and the other compares a
cubic and exponential function. Both plots also employ the pylab function legend(), which allows us to 
visualize which curve relates to which dataset.

Created on Tue Nov 13 13:30:39 2018

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
    

# Generate linear vs quadratic plot
plt.figure("lin quad")
plt.clf() # clears the frame
plt.ylim(0, 1000)
plt.plot(mySamples, myLinear, "b-", label="linear") # b- means blue line
plt.plot(mySamples, myQuadratic, "ko", label="quadratic") # ko means black dots
plt.legend(loc = "upper right") # specifies the location of the legend instead of applying pylab default

# Generate cubic vs exponential plot
plt.figure("cube exp")
plt.clf() # clears the frame
plt.plot(mySamples, myCubic, "r--", label="cubic") # r-- means red dashed
plt.plot(mySamples, myExponential, "g^", label="exponential") # g^ means green triangles
plt.legend() # apply pylab default for legend location

# Title the plots
plt.figure("lin quad")
plt.title("Linear vs. Quadratic")
plt.figure("cube exp")
plt.title("Cubic vs. Exponential")

