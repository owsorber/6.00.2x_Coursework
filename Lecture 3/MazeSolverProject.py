#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the code for my Lecture 3 Project. For my Lecture 3 Project, I decided to create a Maze Solver that uses
Graph Theory and Breadth-First Recursive Searching to find the optimal route to complete the maze.
Since I didn't know of a way to convert a maze image into a graph, I decided to create a maze array that stores a string for
each row of the maze I'm using for testing. Since the maze I'm using is 10 x 10, there are 10 strings of 10 characters.
Each character represents a location along the maze and the possibilities of movements from that location.
Using this array, I built a graph of 100 nodes that are connected if one can move from one to the other in one move
in the maze. Then, I print out the optimal solution to the maze to the screen.

Work in Progress, TODO: 
    * Output optimization data to the user
    * Allow importing of maze images?

Created on Sat Oct 27 22:37:18 2018

@author: owsorber
"""

"""
For each location in the maze, a digit/letter represents the possibilities of next movements.
Every location represents a node. An undirected edge connects every pair of adjacent locations/nodes.

0 = only up
1 = only down
2 = only left
3 = only right
4 = up, down
5 = left, right
6 = up, left
7 = up, right
8 = down, left
9 = down, right
a = can't move up
b = can't move down
c = can't move left
d = can't move right
e = up, down, left, right
"""
mazeArray = [
"95a895aa58",
"7807636c24",
"9b2138369d",
"ca27849240",
"475847b878",
"4356495d14",
"75896417d4",
"9ab696c844",
"0c8143dc64",
"3676720756",
]


class Node:
    def __init__(self, name, possibilities):
        self.name = name
        self.possibilities = possibilities
    
    def getName(self):
        return self.name
    
    def getPossibilities(self):
        return self.possibilities
    
    def __str__(self):
        return str(self.name)
    
class Edge:
    def __init__(self, sourceNode, destinationNode):
        self.src = sourceNode
        self.dest = destinationNode
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + " -> " + self.dest.getName()
    
class Maze:
    def __init__(self, start, end):
        self.edges = {}
        self.start = start
        self.end = end
    
    def addNode(self, node):
        if node in self.edges:
            raise ValueError("This node already exists")
        else:
            self.edges[node] = []
            
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if src not in self.edges:
            raise ValueError("Node isn't in graph")
        else:
            self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name)
    
    # Breadth-first search through maze
    def searchForPath(self):
        pathQueue = [self.start]
        while len(pathQueue != 0):
            tempPath = pathQueue.pop(0)
            lastNode = tempPath[-1]
            if lastNode == self.end:
                return tempPath
            for node in self.childrenOf(lastNode):
                newPath = tempPath + [node]
                pathQueue.append(newPath)
    
    def __str__(self):
        result = ""
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.__str__() + " -> " + dest.__str__() + "\n"
        
        return result
    
maze = Maze(4, 95)

def onlyUp(node):
    maze.addEdge(Edge(node, maze.getNode(node.getName() - len(mazeArray))))

def onlyDown(node):
    maze.addEdge(Edge(node, maze.getNode(node.getName() + len(mazeArray))))
    
def onlyLeft(node):
    maze.addEdge(Edge(node, maze.getNode(node.getName() - 1)))
    
def onlyRight(node):
    maze.addEdge(Edge(node, maze.getNode(node.getName() + 1)))

def buildMaze():
    for i in range(0, len(mazeArray)):
        for j in range(0, len(mazeArray[i])):
            maze.addNode(Node(j + i * len(mazeArray[i]), mazeArray[i][j]))
    
    for node in maze.edges:
        p = node.getPossibilities()
        if p == "0":
            onlyUp(node)
        elif p == "1":
            onlyDown(node)
        elif p == "2":
            onlyLeft(node)
        elif p == "3":
            onlyRight(node)
        elif p == "4":
            onlyUp(node)
            onlyDown(node)
        elif p == "5":
            onlyLeft(node)
            onlyRight(node)
        elif p == "6":
            onlyUp(node)
            onlyLeft(node)
        elif p == "7":
            onlyUp(node)
            onlyRight(node)
        elif p == "8":
            onlyDown(node)
            onlyLeft(node)
        elif p == "9":
            onlyDown(node)
            onlyRight(node)
        elif p == "a":
            onlyDown(node)
            onlyLeft(node)
            onlyRight(node)
        elif p == "b":
            onlyUp(node)
            onlyLeft(node)
            onlyRight(node)
        elif p == "c":
            onlyUp(node)
            onlyDown(node)
            onlyRight(node)
        elif p == "d":
            onlyUp(node)
            onlyDown(node)
            onlyLeft(node)
        elif p == "e":
            onlyUp(node)
            onlyDown(node)
            onlyLeft(node)
            onlyRight(node)
    



buildMaze()
print(maze)