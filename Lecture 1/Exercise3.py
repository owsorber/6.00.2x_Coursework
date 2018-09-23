#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the three problems of Lecture 1 Exercise 3 which ask for the big-O run-time of different Python functions.
For each problem I've written my own explanation of why the answer is as it is for personal reference/comprehension.

Created on Sun Sep 23 14:36:00 2018

@author: owsorber
"""


"""
PROBLEM #1
Answer: n
Explanation: The function takes in a list of n elements and then loops through each element in that list once, meaning the 
for loop will iterate n times. 

"""
NUMBER = 3
def look_for_things(myList):
    """Looks for all elements"""
    for n in myList:
        if n == NUMBER:
            return True
    return False

#############################################################################

"""
PROBLEM #2
Answer: n^2
Explanation: The function takes in a list of n elements. The outer loop iterates n times and the inner loop also iterates 
n times because both loops iterate through myList once. This means we have a big-O runtime of n*n. 

"""
NUMBER = 3
def look_for_other_things(myList):
    """Looks for all pairs of elements"""
    for n in myList:
        for m in myList:
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False

#############################################################################

"""
PROBLEM #3
Answer: 2^n
Explanation: We are asked to ignore the run time of get_all_subsets. A list of n elements has 2^n subsets (including the 
set and the empty set). So, the second function loops through the list of subsets once which means the for loop will 
iterate 2^n times. 

"""
def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

NUMBER = 3
def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False
