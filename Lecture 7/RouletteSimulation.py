#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file simulates a game of Fair Roulette, a casino game in which players can bet that a ball
will roll into a specific pocket or a specific colored pocket. Given the orientation of the
Roulette wheel, the Fair Roulette determines whether a random ball is black or red. It also 
contains functions for betting for certain outcomes that return the amount gained or lost.
Then, playRoulette() plays a game of FairRoulette for a certain number of spins and prints
the results.
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
        if (self.ball > 0 and self.ball <= 10) or (self.ball > 18 and self.ball <= 28):
            return self.ball % 2 == 0 # if pocket is even and in these ranges, pocket is black
        else:
            return self.ball % 2 == 1 # if pocket is odd and not in these ranges, pocket is red
        
    def isRed(self):
        return not self.isBlack()
    
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
        

def playRoulette(game, numSpins):
    luckyNumber = "2" # Pocket we're betting for the simulation
    
    bet = 1 # Money we're betting for the simulation
    
    totalRed, totalBlack, totalPocket = 0.0, 0.0, 0.0
    
    for i in range(numSpins):
        game.spin()
        totalRed += game.betRed(bet)
        totalBlack += game.betBlack(bet)
        totalPocket += game.betPocket(luckyNumber, bet)
    
    # Print simulation values
    print(numSpins, "spins of", game)
    print("Average Return of betting red:", str(100*totalRed/numSpins), "%")
    print("Average Return of betting black:", str(100*totalBlack/numSpins), "%")
    print("Average Return of betting", luckyNumber, ":", str(100*totalPocket/numSpins), "%")
    
    
numSpins = 100000
game = FairRoulette()
playRoulette(game, numSpins)    
    
