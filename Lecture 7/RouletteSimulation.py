#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file simulates a game of Roulette, a casino game in which players can bet that a ball
will roll into a specific pocket or a specific colored pocket. FairRoulette contains functions 
for betting for certain outcomes that return the amount gained or lost. European Roulette is a
subclass of FairRoulette with an extra pocket, "0", and American Roulette is a subclass of
EuropeanRoulette with an extra pocket "00". Then, playRoulette() plays a game for a certain 
number of spins and getPocketReturns() gets the returns of betting on a pocket for a game.
Then, the sample mean with confidence intervals is printed out to show that playing in American 
or European Roulette yields worse outcomes than Fair Roulette.
Code inspired by Lecture 7 of MIT Course 6.00.2x

Created on Fri Jan 4 15:01:11 2019

@author: owsorber
"""

import random

class FairRoulette:
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        
        self.ball = None # the ball dropped in the roulette wheel
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) - 1
        
    
    # Picks a random pocket
    def spin(self):
        self.ball = random.choice(self.pockets)
    
    # Uses the configuration of a roulette wheel to determine black and red pockets
    def isBlack(self):
        if type(self.ball) != int:
            return False
        
        if (self.ball > 0 and self.ball <= 10) or (self.ball > 18 and self.ball <= 28):
            return self.ball % 2 == 0 # if pocket is even and in these ranges, pocket is black
        else:
            return self.ball % 2 == 1 # if pocket is odd and not in these ranges, pocket is red
        
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()
    
    # Bet on a color or pocket.
    # If you win, you get the odds times your bet. If you lose, you lose the money you bet.
    def betBlack(self, amt):
        if self.isBlack():
            return amt * self.blackOdds
        else:
            return -amt
    def betRed(self, amt):
        if self.isRed():
            return amt * self.redOdds
        else:
            return -amt
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt
        
    def __str__(self):
        return "Fair Roulette"


def playRoulette(game, numSpins, toPrint):
    luckyNumber = "2" # Pocket we're betting for the simulation
    
    bet = 1 # Money we're betting for the simulation
    
    totalRed, totalBlack, totalPocket = 0.0, 0.0, 0.0
    
    for i in range(numSpins):
        game.spin()
        totalRed += game.betRed(bet)
        totalBlack += game.betBlack(bet)
        totalPocket += game.betPocket(luckyNumber, bet)
    
    # Print simulation values
    if toPrint:
        print(numSpins, "spins of", game)
        print("Average Return of betting red:", str(100*totalRed/numSpins), "%")
        print("Average Return of betting black:", str(100*totalBlack/numSpins), "%")
        print("Average Return of betting", luckyNumber, ":", str(100*totalPocket/numSpins), "%")
    
    return (totalRed/numSpins, totalBlack/numSpins, totalPocket/numSpins)
    
   
# Sub classes of Fair Roulette to represent European Roulette and American Roulette
class EuropeanRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append("0")
    
    def __str__(self):
        return "European Roulette"  
class AmericanRoulette(EuropeanRoulette):
    def __init__(self):
        EuropeanRoulette.__init__(self)
        self.pockets.append("00")
    
    def __str__(self):
        return "American Roulette"   

def findPocketReturn(game, numTrials, trialSize):
    pocketReturns = []
    for trial in range(0, numTrials):
        trialVals = playRoulette(game, trialSize, False)
        pocketReturns.append(trialVals[2])
    return pocketReturns


def getMeanAndStd(sample):
    mean = sum(sample) / float(len(sample))
    tot = 0.0
    for x in sample:
        tot += (x - mean) ** 2
    stdev = (tot/len(sample)) ** 0.5
    return mean, stdev


# Testing out a game of fair roulette
#numSpins = 10
#game = FairRoulette()
#playRoulette(game, numSpins)    
    
numTrials = 20
games = (FairRoulette, EuropeanRoulette, AmericanRoulette)
resultDict = {}

for game in games:
    resultDict[game().__str__()] = [] # set each key game name to an empty list

for numSpins in (100, 1000, 10000, 100000):
    print("\nSimulate betting pocket for", numTrials, "trials of", numSpins, "spins each")
    for game in games:
        pocketReturns = findPocketReturn(game(), numTrials, numSpins)
        mean, std = getMeanAndStd(pocketReturns)
        resultDict[game().__str__()].append((numSpins, 100*mean, 100*std))
        print("Expected return for", game(), "is", str(round(100*mean, 3)), "%", "+/-", str(round(100*1.96*std, 3)), "%", "with 95% confidence")
        
    
    
