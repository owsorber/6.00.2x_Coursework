#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is an exploration of two different methods of determining the nth term of the Fibonacci sequence. Both use 
recursion, but the second one employs the use of memoization, which means is stores the return values of previous calls 
of FastFib.
Code inspired by Lecture 2 of MIT Course 6.00.2x: Introduction to Computational Thinking and Data Science

Created on Tue Oct 2 21:09:34 2018

@author: owsorber
"""

# This is a classic recursive algorithm to compute the nth term in the Fibonacci sequence.
# However, it is very inefficient, and the runtime grows as the value of the term we're trying to find grows.
def fib(n):
    if n == 1 or n == 0:
        return n
    
    return fib(n - 1) + fib(n - 2)


# FASTER FIBONACCI ALGORITHM
def fastFib(n, memo = {}):
    if n == 1 or n == 0:
        return n
    
    """ If a value of key "n" already exists in memo, we return it because that means we already calculated it in 
    a previous method call """
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result # Store result in memo with key "n" so that we can reference it later
        return result

    
# This will run really fast because of memoization. Note: we are sacrificing space for time.
for n in range(1, 101):
    print("Fib(" + str(n) + ") = " + str(fastFib(n)))
