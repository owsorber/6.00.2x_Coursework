#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains two search methods that build upon the Graph Theory used in previous files to find the optimal
path between a starting node and an ending node. One method employs a depth-first search, which means it looks at the
first child of the starting node and then recursively keeps looking for a path consisting of that first child. If
no path is found, the method backtracks and looks at the second child, and so on. The other method employs a
breadth-first search which starts at the starting node and puts each child in the path queue to explore them next
and keeps moving down along the reachable nodes until one finds the solution. The first found solution will be the shortest.
Created on Wed Oct 17 07:47:10 2018

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


""" New Code """

"""
depthFirstSearch Parameters:
graph: the graph we are searching
start: the starting node
end: the destination node
path: the current path from some start node to another node we are exploring
shortest: the shortest path from start to end we've found so far
"""
def depthFirstSearch(graph, start, end, path, shortest):
    path += [start] # add starting node to current path we're exploring
    if start == end:
        return path # this path has reached the desired node, so return it
    
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest): # only explore this node if its path is shorter than shortest
                # the node we're currently looking at is the new "start" for the method
                newPath = depthFirstSearch(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath # if there exists a new path, assign it to shortest
            
    return shortest # return shortest so far if the path was able to exit the loop as less than previous shortest
    

def breadthFirstSearch(graph, start, end):
    pathQueue = [start]
    while len(pathQueue != 0):
        tempPath = pathQueue.pop(0) # take out next in queue and store it in tempPath
        lastNode = tempPath[-1] # last element of tempPath list
        if lastNode == end:
            return tempPath
        for nextNode in graph.childrenOf(lastNode):
            newPath = tempPath + [nextNode]
            pathQueue.append(newPath)
            
    return None
            


def shortestPath(graph, start, end):
    return depthFirstSearch(graph, start, end, [], None)
    
    
    
    
