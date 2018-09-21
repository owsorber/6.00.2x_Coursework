#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is a basic Python test using the Spyder Python Development Environment.

Created on Sat Sep 15 23:10:59 2018

@author: owsorber
"""

import random

print("Hello world!")
print ("I love 6.00.2x!")

excitedness = 10

def excited_string(excited_index):
    if excited_index == 10:
        return "I AM SO EXCITED FOR THIS COURSE!"
    else:
        return "I'm ready to begin."

print(excited_string(excitedness))


suits = ("Hearts", "Spades", "Diamonds", "Clubs")
class Card:
    num = None
    suit = None
    
    def __init__(self, number, suit):
        self.num = number
        self.suit = suit
    
    def set_suit(self, newSuit):
        self.suit = newSuit
        
    def get_suit(self):
        return self.suit
    
    def set_num(self, newNum):
        self.num = newNum
    
    def get_num(self):
        return self.num
    
    def toString(self):
        return "%s of %s" % (self.num, self.suit)
    
randomNum = random.randint(1, 11)


card = Card(randomNum, suits[random.randint(0, 4)])

print("I have a %s" % card.toString())
