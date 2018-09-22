#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains two classes: Item and Knapsack and uses a greedy algorithm to approximate an optimal solution for which Items to place in the knapsack.
Code inspired by Lecture 1 of MIT Course 6.00.2x: Introduction to Computational Thinking and Data Science

Created on Thu Sep 20 13:23:00 2018

@author: owsorber
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
    def __init__(self, mw, metric, available):
        self.maxWeight = mw # maximum weight that the knapsack can carry
        self.availableItems = sorted(available, key = metric, reverse = True) # list of all available Item objects sorted from best to worst
        self.takenItems = [] # list to indicate whether each item is taken
        self.metric = metric # metric used to determine next most valuable item
        for i in range(0, len(self.availableItems)):
            self.takenItems.append(0)
            
        self.totalWeight = 0
        self.totalValue = 0
            
    
    # Greedy algorithm (runs through each available item and adds it to knapsack if it fits based on maxWeight)
    def greedy(self):
        for i in range(0, len(self.availableItems)):
            if self.totalWeight + self.availableItems[i].getWeight() <= self.maxWeight:
                self.takenItems[i] = 1
                self.totalWeight += self.availableItems[i].getWeight()
                self.totalValue += self.availableItems[i].getValue()
                #print(self.availableItems[i].toString())
    
    def toString(self):
        string = "Total Value: " + str(self.totalValue) + ", Total Weight: " + str(self.totalWeight) + "\n"
        string += "Items Taken:\n"
        for i in range(0, len(self.availableItems)):
            if self.takenItems[i] == 1:
                string += "\t" + self.availableItems[i].toString() + "\n"
        return string
            

# In this case, each item is a food: value is determined by relative deliciousness and weight is caloric value
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

knapsackByValueDensity = Knapsack(1000, Item.valueDensity, items)
knapsackByValue = Knapsack(1000, Item.getValue, items)
knapsackByWeight = Knapsack(1000, lambda x: 1/Item.getWeight(x), items)

#Test each greedy algorithm
knapsackByValueDensity.greedy()
print("Greedy By Value Density:\n" + knapsackByValueDensity.toString() + "\n")
knapsackByValue.greedy()
print("Greedy By Value:\n" + knapsackByValue.toString() + "\n")
knapsackByWeight.greedy()
print("Greedy By Weight:\n" + knapsackByWeight.toString() + "\n")

