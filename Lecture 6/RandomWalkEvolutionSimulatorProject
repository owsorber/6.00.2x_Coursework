#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the code for my Lecture 6 Project. For my Lecture 6 Project, I decided to create
a simple Evolution Simulator that uses Charles Darwin's Theory of Natural Selection. The organisms
in this simulation are random walkers represented by 1D points that move along a 2D coordinate plane.
Their purpose in life is to get to a desired position after a certain amount of steps, and their 
movement is dictated by their traits, each trait being a vector representing a single step. 
After each generation is simulated, those that end closest to the desired position are most fit 
for survival and most likely to pass on their genes, which they do asexually to form the next 
generation.

One can tune several different constants of evolution, such as the desired position, the number of
steps, the survival rate, the likelihood of mutations, the number of organisms per generation,
the number of traits, and the number of generations to simulate. The program then generates that 
number of generations and displays their data in the form of print statements and plots.

Potential TODOs:
    * Enable sexual reproduction in which best fit organisms are randomly assigned to a mate
    * Offer other incentives for the organisms such as multiple "desired" points
    * Allow visualization of best organism's entire path per generation

Created on Mon Dec 3 13:50:57 2018

@author: owsorber
"""

import random
import math
import pylab as plt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        return Vector(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        deltaX = self.x - other.getX()
        deltaY = self.y - other.getY()
        return math.sqrt(deltaX ** 2 + deltaY ** 2)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    

""" CONSTANTS OF EVOLUTION - CHANGE THESE FOR DIFFERENT RESULTS """

STARTING_POSITION = Vector(0, 0) # Each organism's starting position
DESIRED_POSITION = Vector(1000, 1000)
NUM_STEPS = 100 # Number of steps an organism takes throughout random walk

START_TRAIT_RANGE = (-1, 1) # Range of potential start traits, which are generated randomly
SURVIVAL_RATE = 0.01 # Rate of survival
MUTATION_CONSTANT = 0.2 # Range of potential mutation

ORGANISMS_PER_GENERATION = 100 # Organisms per generation (runtime decreases as # increases)
NUMBER_TRAITS = 1 # Number of traits to dictate organism movement

NUMBER_GENERATIONS = 1000 # Number of generations to simulate
PLOT_FREQUENCY = 200 # Generate a plot for every nth generation
DATA_FREQUENCY = 200 # Show data for every nth generation


class Organism:
    def __init__(self, idNum, parentTraits):
        self.idNum = idNum
        self.generationNum = self.idNum // 100 + 1
        
        if self.generationNum == 1:
            self.traits = parentTraits
        else:
            # Generate traits through random mutation of parent's traits
            self.traits = []
            for trait in parentTraits:
                randomMutationX = round(random.uniform(-MUTATION_CONSTANT, MUTATION_CONSTANT), 4)
                randomMutationY = round(random.uniform(-MUTATION_CONSTANT, MUTATION_CONSTANT), 4)
                self.traits.append(trait.move(randomMutationX, randomMutationY))
    
    def getID(self):
        return self.idNum
    
    def getTraits(self):
        return self.traits
    
    def takeStep(self):
        return random.choice(self.traits)
    
    def __str__(self):
        traits = ""
        for trait in self.traits:
            traits += trait.__str__() + ", "
        return "Organism # " + str(self.idNum)
    
class Generation:
    def __init__(self, num):
        self.num = num
        self.organisms = {} # maps an organism to a location
    
    # Generates the generation from the previous generation
    def generate(self, previousGeneration):
        if self.num == 1:
            for i in range(1, ORGANISMS_PER_GENERATION + 1):
                traits = []
                for traitNum in range(0, NUMBER_TRAITS):
                    traits.append(Vector(round(random.uniform(START_TRAIT_RANGE[0], START_TRAIT_RANGE[1]), 4), round(random.uniform(START_TRAIT_RANGE[0], START_TRAIT_RANGE[1]), 4)))
                self.organisms[Organism(i, traits)] = STARTING_POSITION
        else:
            idNum = (self.num - 1) * 100 + 1
            for parent in previousGeneration.kill():
                for i in range(0, int(1/SURVIVAL_RATE)):
                    self.addOrganism(Organism(idNum, parent.getTraits()))
                    idNum += 1
    
    def addOrganism(self, organism):
        self.organisms[organism] = STARTING_POSITION
    
    # Runs a random walk for each organism
    def randomWalk(self):
        for organism in self.organisms:
            for step in range(0, NUM_STEPS):
                self.moveOrganism(organism)
    
    # Returns the list of organisms in a generation after the least fit 50 get killed
    def kill(self):
        sortedList = self.organismsSorted()
        for i in range(0, int((1-SURVIVAL_RATE) * ORGANISMS_PER_GENERATION)):
            sortedList.pop(0)
        return sortedList
    
    def plotGeneration(self):
        desiredX = [DESIRED_POSITION.getX()]
        desiredY = [DESIRED_POSITION.getY()]
        xVals = []
        yVals = []
        
        for organism in self.organisms:
            xVals.append(self.getPosition(organism).getX())
            yVals.append(self.getPosition(organism).getY())
        
        plt.figure("Generation " + str(self.num))
        plt.clf()
        plt.title("Final Positions for Generation # " + str(self.num))
        plt.xlabel("X")
        plt.ylabel("Y")
        #plt.xlim(-100, 1200)
        #plt.ylim(-100, 1200)
        plt.plot(xVals, yVals, "r^")
        plt.plot(desiredX, desiredY, "bo")
    
    def moveOrganism(self, organism):
        choiceMove = organism.takeStep()
        deltaX = choiceMove.getX()
        deltaY = choiceMove.getY()
        self.organisms[organism] = self.getPosition(organism).move(deltaX, deltaY)

    # Returns a list of the organisms, sorted from worst survival chance to best
    def organismsSorted(self):
        sortedList = []
        while len(sortedList) < ORGANISMS_PER_GENERATION:
            currWorstDistance = 0
            currWorstOrganism = None
            for organism in self.organisms:
                organismPosition = self.getPosition(organism)
                organismDistanceFrom = organismPosition.distFrom(DESIRED_POSITION)
                if organismDistanceFrom > currWorstDistance and organism not in sortedList:
                    currWorstDistance = organismDistanceFrom
                    currWorstOrganism = organism
            
            sortedList.append(currWorstOrganism)
        return sortedList
    
    # Gets the position of an organism
    def getPosition(self, organism):
        return self.organisms[organism]
    
    def getOrganism(self, idNum):
        for organism in self.organisms:
            if organism.idNum == idNum:
                return organism
    
    def bestOrganism(self):
        organismList = self.organismsSorted()
        return organismList[len(organismList) - 1]
    
    def averageDistance(self):
        avgDist = 0
    
        for organism in self.organisms:
            avgDist += self.getPosition(organism).distFrom(DESIRED_POSITION)
        
        avgDist /= ORGANISMS_PER_GENERATION
        
        return avgDist
    
    def __str__(self):
        output = ""
        for organism in self.organisms:
            output += organism.__str__() + "\n"
        
        return output
        

    
generations = []

for i in range(0, NUMBER_GENERATIONS):
    genNum = i + 1
    genIndex = i
    prevGenIndex = i - 1
    
    generations.append(Generation(genNum))
    generations[genIndex].generate(generations[prevGenIndex])
    print("Generation %s has been generated." % str(genNum))
    generations[genIndex].randomWalk()
    print("Generation %s Organisms have completed their random walk." % str(genNum))
    
    
    if i == 0 or i % DATA_FREQUENCY == DATA_FREQUENCY - 1:
        avgDistance = round(generations[genIndex].averageDistance(), 4)
        print("Generation %s Average Distance: " % str(genNum) + str(avgDistance))
        
        
        bestOrg = generations[genIndex].bestOrganism()
        print("Generation %s Best Organism: " % str(genNum))
        print(str(bestOrg) + " with distance: " + str(generations[genIndex].getPosition(bestOrg).distFrom(DESIRED_POSITION)))
    
    print()
    
    if i == 0 or i % PLOT_FREQUENCY == PLOT_FREQUENCY - 1:
        generations[i].plotGeneration()
    
