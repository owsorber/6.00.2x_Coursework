#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains a Node class that has one property, name, and an Edge class that has two properties, a source node 
and a destination node. 
Then, there is a Digraph class that builds a directed graph and has a single dictionary of edges as its instance data. 
This dictionary has keys for each source node which maps the source node to a list of destination nodes.
The Digraph class has methods for adding nodes and edges that allows us to build an entire Digraph. 
The Graph class is a subclass of the Digraph class which overrides the addEdges method so that each edge is symmetrical, 
which would be the case for an undirected graph.
Code inspired by Lecture 3 of MIT Course 6.00.2x: Introduction to Computational Thinking and Data Science

Created on Sun Oct 14 21:13:27 2018

@author: owsorber
"""

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
    
""" Directed Graph """
class Digraph(object): # inheritance, same as "extends Object" in Java
    def __init__(self):
        self.edges = {} # edges is a dictionary that maps a source node to destination nodes
        
    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate node") # if node is already in the dictionary, tell us this new node is a duplicate
        else:
            self.edges[node] = [] # otherwise, add an empty list to the edges dictionary with key node
    
    def addEdge(self, edge):
        src = edge.getSource() # conveniently store this edge's source node in src
        dest = edge.getDestination() # conveniently store this edge's destination node in dest
        if src in self.edges:
            # if there is a list in the edges dictionary with key src, then we can add dest to the list of destination nodes
            self.edges[src].append(dest) 
        else:
            raise ValueError("Node not in graph") # otherwise, tell us this edge's source node is not currently in our graph
            
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
    
""" Undirected Graph """
class Graph(Digraph): # Graph inherits digraph and overrides addEdge method
    """ 
    Graph's addEdge calls the Digraph addEdge method twice:
        Once for the original directed edge, and once for the reverse of the edge (this makes it a symmetrical edge)
    """
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        reverseEdge = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, reverseEdge)


""" Example of Digraph using cities """

# Create list of names that correspond to each of the 7 nodes
cityNames = ["Boston", "Providence", "New York", "Chicago", "Denver", "Phoenix", "Los Angeles"]

digraph = Digraph() # if this was Graph(), then each edge would be symmetrical
for name in cityNames:
    digraph.addNode(Node(name))

# Add a directed edge to connect each pair of nodes as shown in the image of cities
digraph.addEdge(Edge(digraph.getNode('Boston'), digraph.getNode('Providence')))
digraph.addEdge(Edge(digraph.getNode('Boston'), digraph.getNode('New York')))
digraph.addEdge(Edge(digraph.getNode('Providence'), digraph.getNode('Boston')))
digraph.addEdge(Edge(digraph.getNode('Providence'), digraph.getNode('New York')))
digraph.addEdge(Edge(digraph.getNode('New York'), digraph.getNode('Chicago')))
digraph.addEdge(Edge(digraph.getNode('Chicago'), digraph.getNode('Denver')))
digraph.addEdge(Edge(digraph.getNode('Denver'), digraph.getNode('Phoenix')))
digraph.addEdge(Edge(digraph.getNode('Denver'), digraph.getNode('New York')))
digraph.addEdge(Edge(digraph.getNode('Los Angeles'), digraph.getNode('Boston')))


print(digraph)

