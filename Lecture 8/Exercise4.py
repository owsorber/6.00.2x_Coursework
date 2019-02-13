#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains my solution to Lecture 8 Exercise 4.
The noReplacementSimulation draws 3 balls out of a bucket of 3 green balls and 3 red balls.
Then, the proportion of trials where all 3 balls were the same color is computed in simulation.
I used a list bucket where 1s represent one color and 0s represent another. I then used a loop
to build the selected list until a different color is selected (indicating a failure) or the 
selected list reaches a length of 3 (indicating there was never a ball of different color 
added).

Created on Wed Feb 13 13:27:14 2019

@author: owsorber
"""

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numSuccesses = 0
    for trial in range(numTrials):
        bucket = [1, 1, 1, 0, 0, 0]
        selected = []
        for i in range(3):
            choiceIndex = random.randint(0, len(bucket) - 1)
            choice = bucket[choiceIndex]
            if len(selected) > 0 and choice not in selected:
                break;
            selected.append(choice)
            bucket.pop(choiceIndex)
        
        if len(selected) == 3:
            numSuccesses += 1
    
    return numSuccesses / numTrials


# TESTING - NOT PART OF SOLUTION TO EXERCISE
print(noReplacementSimulation(10000))
    
