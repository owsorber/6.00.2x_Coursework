#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file follows Lecture 4 Segment 6 which provides a practical example of plotting using the pylab
library. The retire function returns a dataset of x and y values for how much money put towards
retirement an individual has at each month depending on how much is put aside per month, what the
interest rate is, and the amount of months to compute over. Then, the following three functions
create plots that analyze the result of changing the monthly investment, interest rate, or both
on the retirement savings.

Created on Tue Nov 13 15:37:52 2018

@author: owsorber
"""

import pylab as plt

# Parameters: monthly (amount put aside each month), rate (interest rate), terms (how many months/terms to compute over)
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    
    for i in range(terms):
        base += [i] # x values (current month in the computation)
        savings += [savings[-1] * (1 + mRate) + monthly] # y values (how much money we've saved by this month)
    return base, savings

# plot a curve for each monthly investment in monthlies list
def displayRetireWithMonthlies(monthlies, rate, terms):
    plt.figure("retireMonth")
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.xlabel("Month #")
        plt.ylabel("Money Saved ($)")
        plt.plot(xvals, yvals, label = "retire with $" + str(monthly) + " put aside per month")
        plt.legend(loc = "upper left")

# plot a curve for each interest rate in rates list
def displayRetireWithRates(monthly, rates, terms):
    plt.figure("retireRate")
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(monthly, rate, terms)
        plt.xlabel("Month #")
        plt.ylabel("Money Saved ($)")
        plt.plot(xvals, yvals, label = "interest rate: " + str(100*rate) + "%")
        plt.legend(loc = "upper left")

# plot a curve for each pair of monthly investment and interest rate from monthlies and rates
def displayRetireWithMonthliesAndRates(monthlies, rates, terms):
    plt.figure("retireBoth")
    plt.clf()
    plt.xlim(0.75*terms, terms) # set the x range to only be the last quarter of data
    monthlyLabels = ["r", "g", "b", "k"] # dictate the colors of each curve for easier visualization
    rateLabels = ["-", "o", "--"] # dicate the format of each curve for easier visualization
    for m in range(len(monthlies)):
        monthly = monthlies[m]
        monthlyLabel = monthlyLabels[m % len(monthlyLabels)]
        for r in range(len(rates)):
            rate = rates[r]
            rateLabel = rateLabels[r % len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.xlabel("Month #")
            plt.ylabel("Money Saved ($)")
            plt.plot(xvals, yvals, 
                     monthlyLabel+rateLabel, 
                     label = "$" + str(monthly) + ", " + str(100*rate) + "% rate")
            plt.legend(loc = "upper left")

# Monthlies and Rates lists for plotting
monthlies = [500, 700, 900, 1100]
rates = [0.02, 0.05, 0.08]

displayRetireWithMonthlies(monthlies, 0.05, 40*12)
displayRetireWithRates(500, rates, 40*12)
displayRetireWithMonthliesAndRates(monthlies, rates, 40*12)

