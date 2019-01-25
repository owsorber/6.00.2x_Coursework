#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file plots a normal distribution of random mean and random standard deviation using the
pylab library. Then, the function checkEmpirical integrates the normal distribution equation
using the scipy.integrate library to determine whether the percentages of a normal distribution 
within z values of 1, 2, and 3 are really 68%, 95%, and 99.7% respectively.
Code inspired by Lecture 7 of MIT Course 6.00.2x

Created on Thu Jan 24 22:12:12 2019

@author: owsorber
"""

import pylab
import random
import scipy.integrate
import math

def plotNormalDistribution(mu, std):
    dataset = []
    for i in range(0, 100000):
        dataset.append(random.gauss(mu, std))
    
    pylab.title("Normal Model")
    pylab.hist(dataset, 60) # plots a histogram with dataset of 30 buckets
    

plotNormalDistribution(0, 1)


def probability(x, mu, sigma):
    factor1 = 1.0 / (sigma) / ((2*math.pi) ** 0.5)
    factor2 = math.e ** -(((x-mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print("For mean =", mu, "and std =", sigma)
        for z in (1.0, 2.0, 3.0):
            area = scipy.integrate.quad(probability, mu-z*sigma, mu+z*sigma, (mu, sigma))[0] * 100
            print("Percent within", z, "standard deviations of mean:", round(area, 4))
        
        print()
    

checkEmpirical(3)
