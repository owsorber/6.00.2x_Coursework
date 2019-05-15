#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

def getPerformanceData(fname):
    training_lengths = []
    accuracies = []
    times = []
    num_trials = []
    
    file = open(fname, "r")
    for line in file.read().splitlines()[1:]:
        tl, acc, time, trials = line.split(", ")
        training_lengths.append(float(tl))
        accuracies.append(float(acc))
        times.append(float(time))
        num_trials.append(float(trials))
    
    return training_lengths, accuracies, times, num_trials


training_lengths, accuracies, times, num_trials = getPerformanceData("PerformanceData.txt")

def plotAccuracy():
    plt.figure("Accuracy")
    plt.plot(training_lengths, accuracies, "b")
    plt.title("Prediction Accuracy vs. Size of Training Data")
    plt.xlabel("# of Digits Trained On")
    plt.ylabel("Percent Correct")
    plt.show()

def plotTimes():
    plt.figure("Time")
    plt.plot(training_lengths, times, "r")
    plt.title("Prediction Time vs. Size of Training Data")
    plt.xlabel("# of Digits Trained On")
    plt.ylabel("Time per Prediction")
    plt.show()
        
plotAccuracy()
plotTimes()
