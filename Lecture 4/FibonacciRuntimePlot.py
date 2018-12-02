#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file uses the Python pylab library to build a plot that graphs the runtime of the 
Fibonacci recursive algorithm vs. the number term being computed. The graph corroborates
the exponentiality of this recursive algorithm and is an interesting simulation.

Created on Wed Nov 28 08:32:57 2018

@author: owsorber
"""

import pylab as plt
import time

# Finds the nth term in the fibonacci sequence
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
    

def createPlot(termNums):
    xvals = []
    yvals = []
    
    plt.figure("fibonacci-runtime")
    plt.clf()
    plt.title("Runtime of Fibonacci Recursive Algorithm")
    for n in termNums:
        xvals.append(n)
        start = time.time()
        print(str(n) + ": " + str(fibonacci(n)))
        end = time.time()
        yvals.append(end - start)

    plt.xlabel("Term # in Fibonacci Sequence")
    plt.ylabel("Runtime in seconds")
    plt.plot(xvals, yvals)
        
    
createPlot([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])
