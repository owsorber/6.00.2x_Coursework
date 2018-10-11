#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the code for my Lecture 2 Project. For my Lecture 2 Project, I decided to solve the Recursive Staircase
Problem. Assume you're given a staircase of N steps. There are only two means by which you can go up the staircase.
Given you can either go "a" steps at a time or "b" steps at a time, how many ways are there to get up the staircase?
TODO: 
    * Enable the algorithm to also return each distinct way to get up the staircase
    * Enable the algorithm to take in a tuple with more than two options

Created on Tue Oct 09 22:54:07 2018

@author: owsorber
"""

"""
Takes in: 
    N (the number of steps on the staircase)
    options (a tuple containing the different numbers of steps at a time that one can go up the staircase)

Returns an int that represents the number of ways one can go up the staircase of N steps.

What's really cool about this is it ends up generating a fibonacci sequence with starting terms option1, option2.
If option1 and option2 are the tuple (1, 2) then numWays(N, options) will be the (N - 1)th term in the Fibonacci sequence.
"""
def numWays(N, options):
    if N <= 0:
        return 0
    elif N == options[0]:
        return 2 if options[0] % options[1] == 0 else 1
    elif N == options[1]:
        return 2 if options[1] % options[0] == 0 else 1
        
    result = numWays(N - options[0], options) + numWays(N - options[1], options)
    return result
    
"""
This method does the same thing as numWays but using memoization to store previously computed results.
"""
def fastNumWays(N, options, memo = {}):
    if N in memo:
        return memo[N]
    elif N <= 0:
        return 0
    elif N == options[0]:
        return 2 if options[0] % options[1] == 0 else 1
    elif N == options[1]:
        return 2 if options[1] % options[0] == 0 else 1
        
    result = fastNumWays(N - options[0], options) + fastNumWays(N - options[1], options)
    memo[N] = result
    return result


testedN = 60
ways = fastNumWays(testedN, (3, 4))

print("For %s stairs, there are %s ways." % (testedN, ways))
