#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the given code for Lecture 3 Exercise 2 as well as my solution to the exercise.

The given classes are the same classes for a Node, Edge, Digraph, and Graph from Segment 2 of Lecture 1.
Using a set of nodes of three letters each, I used nested for loops to only pair nodes that were one adjacent swap from
having the same name.
Created on Tue Oct 16 21:19:25 2018

@author: owsorber
"""

""" Classes Used in Exercise's Given Code """

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
    
class Digraph(object):
    def __init__(self):
        self.edges = {} 
        
    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate node")
        else:
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if src in self.edges:
            self.edges[src].append(dest) 
        else:
            raise ValueError("Node not in graph")
            
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        
        raise NameError(name)
        
    def __str__(self):
        result = ""
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getName() + " -> " + dest.getName() + "\n"
        
        return result
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        reverseEdge = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, reverseEdge)
        
   
     
""" Begin Given Code """
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


""" EXERCISE """
for i in range(0, len(nodes)):
    for j in range(i, len(nodes)):
        node1Name = nodes[i].getName()
        node2Name = nodes[j].getName()
        
        if node1Name == (node2Name[1] + node2Name[0] + node2Name[2]) or node1Name == (node2Name[0] + node2Name[2] + node2Name[1]):
            g.addEdge(Edge(nodes[i], nodes[j]))
            
# TEST for loop (Not part of solution to exercise)
print(g)


