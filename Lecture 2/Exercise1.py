#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the given code for Lecture 2 Exercise 1 as well as my solution to the exercise.

Given is the function powerSet, which takes in a list of items and generates the power set of the list.
The function powerSet uses a binary integer i where each bit represents an item. It loops through all potential 
combinations of bits.
If the bit corresponding to item j (the jth bit) is a 1, the item is taken into the subset. Otherwise, the item is not.

My solution is the code for the function yieldAllCombos. It also uses an integer i but each item is instead represented as a
"trinary" bit: 0 means the item is not taken, 1 means the item goes into bag1, and 2 means the item goes into bag2.
Each bag is represented as a list of items and the lists are yielded at the end as a tuple.
Note: I cannot use the bitwise operators in my solution because integer i is not represented in binary for the purposes 
of this solution (since it has "ternary" bits).

Created on Sat Sep 29 14:59:36 2018

@author: owsorber
"""

""" GIVEN CODE """
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


""" EXERCISE """
def yieldAllCombos(items):
    """
        TASK:
        Generate all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yield a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    for i in range(3**N): # We loop through 3**N possible combinations since now each item has 3 possiblities
        bag1, bag2 = ([], [])
        for j in range(N):
            # Look at the jth bit of integer i
            # If the bit is 1, put the jth item into bag1; if the bit is 2, put the jth item into bag2
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)


# TEST yieldAllCombos (Not part of solution to exercise)
allCombos = yieldAllCombos([1,2,3])
for n in allCombos:
    print(n)
