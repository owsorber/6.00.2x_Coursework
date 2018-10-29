#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains two search methods that build upon the Graph Theory used in previous files to find the optimal
path between a starting node and an ending node. One method employs a depth-first search, which means it looks at the
first child of the starting node and then recursively keeps looking for a path consisting of that first child. If
no path is found, the method backtracks and looks at the second child, and so on. The other method employs a
breadth-first search which starts at the starting node and keeps track of multiple different paths, one for each child.
The method keeps moving down along the reachable nodes until one finds the solution.
The first found solution will be the shortest.
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
    initPath = [start]
    pathQueue = [initPath] # list of paths we explore, all leaving the first node
    while len(pathQueue != 0):
        tempPath = pathQueue.pop(0) # get the next path to explore and store in tempPath
        lastNode = tempPath[-1] # get the last node of the path we're currently exploring
        if lastNode == end:
            return tempPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tempPath:
                newPath = tempPath + [nextNode]
                # add the new path to the queue (note: it was taken out as tempPath earlier in the while loop)
                pathQueue.append(newPath)
            
    return None
            


def shortestPath(graph, start, end):
    return depthFirstSearch(graph, start, end, [], None)

