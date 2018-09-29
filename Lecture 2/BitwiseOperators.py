#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is my breakdown of the different Python bitwise operators (<<, >>, &, |, ~, ^), which I needed to learn before 
completing exercise 1 of lecture 2.
Documentation can be found here: https://wiki.python.org/moin/BitwiseOperators

Created on Fri Sep 28 22:20:30 2018

@author: owsorber
"""


"""
AND Operator: &
For each bit in a and b, the corresponding ouput bit is 1 if both the bit for a AND the bit for b are both 1. 
Otherwise, the corresponding output bit is 0.

OR Operator: |
For each bit in a and b, the corresponding ouput bit is 1 if either the bit for a OR the bit for b is 1. 
Otherwise, the corresponding output bit is 0.
"""
a = 50    # 1100101
b = 25    # 0101001

c = a & b # 0100000
d = a | b # 1101101


"""
RIGHT SHIFT Operator: >>
Each bit in x will be shifted to the right y spaces, and a y number of 0s will show up at the front of the binary expression.
This is equivalent to dividing x by 2^y.

LEFT SHIFT Operator: <<
Each bit in x will be shifted to the left y spaces, and a y number of 0s will show up at the end of the binary expression.
This is equivalent to multiplying x by 2^y.
"""
x = 240     # 11110000
y = 2
rs = x >> y # 00111100
ls = x << y # 11000000


"""
COMPLEMENT Operator: ~
Each 1 of val will be changed to a 0 and each 0 of val will be changed to a 1.
This is equivalent to -val - 1.
"""
val = 100         # 1100100
complement = ~val # 0011011


"""
EXLUSIVE OR Operator: ^
For each bit in m and n, the corresponding output bit is 1 if the bit for m and the bit n are different.
Otherwise, the corresponding output bit is 0.
"""
m = 5          # 0101
n = 12         # 1110
result = m ^ n # 1011
