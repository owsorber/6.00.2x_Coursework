#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains two classes, Item and Knapsack, and uses a decision tree recursive algorithm to find an optimal solution for which 
Items to place in the knapsack.
Code inspired by Lecture 2 of MIT Course 6.00.2x: Introduction to Computational Thinking and Data Science

Created on Fri Sep 28 07:45:50 2018

@author: owsorber1
"""

class Item:
    __name = ""
    __value = 0
    __weight = 0
    
    def __init__(self, name, v, w):
        self.name = name
        self.value = v
        self.weight = w
        
        
    def setValue(self, v):
        self.value = v
        
    def setWeight(self, w):
        self.weight = w
        
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def getName(self):
        return self.name
    
    def toString(self):
        return self.name + ": (%s, %s)" % (self.value, self.weight)
    
    def valueDensity(self):
        return self.value / self.weight



class Knapsack:
    def __init__(self, mw, available):
        self.maxWeight = mw # maximum weight that the knapsack can carry
        self.availableItems = available # a list of all available Item objects to choose from
        
       
    """
    This function takes in a list of items to consider and the weight left in the knapsack.
    Returns tuple: (total value, items chosen)
    It uses recursion to find the optimal solution to the knapsack problem and is exponential in runtime.
    """
    def findOptimal(self, toConsider, availableWeight):
        if toConsider == [] or availableWeight == 0:
            result = (0, ())
        elif toConsider[0].getWeight() > availableWeight:
            result = self.findOptimal(toConsider[1:], availableWeight)
        else:
            currentItem = toConsider[0]
            
            # Explore left branch
            # valueWithItem is total value if item is chosen, withToTake is optimal items chosen if this item is
            valueWithItem, withToTake = self.findOptimal(toConsider[1:], availableWeight - currentItem.getWeight())
            valueWithItem += currentItem.getValue()
            
            #Explore right branch
            # valueWithItem is total value if item isn't chosen, withoutToTake is optimal items chosen if this item isn't
            valueWithoutItem, withoutToTake = self.findOptimal(toConsider[1:], availableWeight)
            
            #Choose better branch
            if valueWithItem > valueWithoutItem:
                result = (valueWithItem, withToTake + (currentItem,))
            else:
                result = (valueWithoutItem, withoutToTake)
        
        return result
    
    
    # Convert the tuple returned from the findOptimal method into a string
    def toString(self):
        optimalSolution = self.findOptimal(self.availableItems, self.maxWeight)
        string = "Total Value: " + str(optimalSolution[0]) + "\n"
        string += "Items Taken:\n"
        for i in optimalSolution[1]:
            string += i.toString() + ", "
        return string
        

items = [
        Item("Wine", 62, 123),
        Item("Beer", 51, 154),
        Item("Pizza", 100, 258),
        Item("Burger", 100, 354),
        Item("Fries", 86, 365),
        Item("Cola", 79, 150),
        Item("Apple", 50, 95),
        Item("Donut", 56, 195)
]

knapsack = Knapsack(1000, items)
print(knapsack.toString())
