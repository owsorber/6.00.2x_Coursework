#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file simulates a random walk through a coordinate plane, represented by the class Field.
Each Field object is a dictionary of Drunks (random walkers) mapped to their locations, and
has methods for moving each Drunk randomly and iterating through the dictionary to find the
Drunk farthest from the origin and closest to the origin, as well as the average distance and
mean final position after the walk has been completed. The function randomWalk() runs through 
a random walk of a certain number of steps for a certain number of drunks.
From this simulation we find that as the number of steps increases, the average distance from 
the origin of all the drunks increases as well.
Code inspired by Lecture 6 of MIT Course 6.00.2x

Created on Sun Dec 2 16:01:09 2018

@author: owsorber
"""

import random
import math


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        return Position(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        deltaX = self.x - other.getX()
        deltaY = self.y - other.getY()
        return math.sqrt(deltaX ** 2 + deltaY ** 2)

    def toString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Drunk:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "The drunk is named " + self.name

class NormalDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return random.choice(stepChoices)

class WinterHatingDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1, 0), (-1, 0), (0, 0.8), (0, -1.2)]
        return random.choice(stepChoices)

class LeftRightDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1, 0), (-1, 0)]
        return random.choice(stepChoices)

class Field:
    def __init__(self):
        self.drunks = {}
    
    # add a drunk to the field
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate Drunk")
        else:
            self.drunks[drunk] = loc
    
    # get the position of a drunk
    def getPosition(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in Field")
        else:
            return self.drunks[drunk]
        
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in Field")
        
        deltaX, deltaY = drunk.takeStep()
        self.drunks[drunk] = self.getPosition(drunk).move(deltaX, deltaY)
        
    def averagePosition(self, numDrunks):
        avgX, avgY = (0, 0)
    
        for drunk in self.drunks:
            avgX += self.getPosition(drunk).getX()
            avgY += self.getPosition(drunk).getY()
        
        avgX /= numDrunks
        avgY /= numDrunks
        
        return avgX, avgY
    
    def averageDistance(self, numDrunks):
        avgDist = 0
    
        for drunk in self.drunks:
            avgDist += self.getPosition(drunk).distFrom(Position(0, 0))
        
        avgDist /= numDrunks
        
        return avgDist
    
    def maxDistance(self):
        maxDist = 0
        for drunk in self.drunks:
            currDrunkDist = self.getPosition(drunk).distFrom(Position(0, 0))
            if currDrunkDist > maxDist:
                maxDist = currDrunkDist
        
        return maxDist
    
    def minDistance(self):
        minDist = self.maxDistance()
        for drunk in self.drunks:
            currDrunkDist = self.getPosition(drunk).distFrom(Position(0, 0))
            if currDrunkDist < minDist:
                minDist = currDrunkDist
        
        return minDist
    

# Runs through a random walk of a certain amount of steps and a certain amount of drunks
def randomWalk(numSteps, numDrunks, drunkClass):
    field = Field()
    
    for i in range(0, numDrunks):
        field.addDrunk(drunkClass(i), Position(0, 0))
    
    # Run through random walk for each drunk
    for drunk in field.drunks:
        for step in range(0, numSteps):
            field.moveDrunk(drunk)
            
    print("Avg Distance: %s" % str(field.averageDistance(numDrunks)))
    print("Min Distance: %s" % str(field.minDistance()))
    print("Max Distance: %s" % str(field.maxDistance()))
    print("Average Position %s" % str(field.averagePosition(numDrunks)))


# Dictionary of all subclasses of drunk mapped to a string identifier
drunkClasses =  {
    NormalDrunk : "Nornal Drunk",
    WinterHatingDrunk : "Winter Hating Drunk",
    LeftRightDrunk : "Left Right Drunk"
}

# Loop through all of our drunk classes and run a random walk
for drunkClass in drunkClasses:
    print(str(drunkClasses[drunkClass]))
    randomWalk(1000, 100, drunkClass)
    print()
    


