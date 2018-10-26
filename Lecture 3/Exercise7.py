#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the given code for Lecture 3 Exercise 7 as well as my solution to the exercise.

Given is the class for a Node and Edge. The task was to write the code for WeightedEdge, a subclass of Edge
that holds a weight as instance data. In the constructor function, weight is initialized along with source
and destination nodes. Then in getWeight, the weight is returned. Finally the __str__ method calls Edge's 
__str__ method and adds an indication of the edge's weight in parentheses.

Created on Thu Oct 25 22:10:41 2018

@author: owsorber
"""

""" Given Code """
class Node(object):
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, sourceNode, destinationNode):
        self.src = sourceNode
        self.dest = destinationNode
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + " -> " + self.dest.getName()


""" EXERCISE """
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        self.src = src
        self.dest = dest
        self.weight = weight
    
    def getWeight(self):
        # Your code here
        return self.weight
    
    def __str__(self):
        # Your code here
        return Edge.__str__(self) + " (" + str(self.weight) + ")"
    

# TEST WeightedEdge Methods (Not part of solution to exercise)
n1 = Node("Node 1")
n2 = Node("Node 2")
weightedEdge = WeightedEdge(n1, n2, 3)

print(weightedEdge)
    
