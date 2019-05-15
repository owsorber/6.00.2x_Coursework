#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FINAL PROJECT - Digit Recognition
"""

import struct as st
import numpy as np
from matplotlib import pyplot as plt
import time
from random import randint


TRAINING_LENGTH = 1000

training_data = {
    "images" : "train-images-idx3-ubyte",
    "labels" : "train-labels-idx1-ubyte"
}

testing_data = {
    "images" : "t10k-images-idx3-ubyte",
    "labels" : "t10k-labels-idx1-ubyte"
}


def getFeaturesArrays(images, labels):
    imagesfile = open(images, "rb")
    labelsfile = open(labels, "rb")

    imagesfile.seek(0)
    labelsfile.seek(8)
    st.unpack('>4B', imagesfile.read(4))

    nImg = st.unpack('>I', imagesfile.read(4))[0] #num of images
    nR = st.unpack('>I', imagesfile.read(4))[0] #num of rows
    nC = st.unpack('>I', imagesfile.read(4))[0] #num of column

    images_array = np.zeros((nImg,nR,nC))
    nBytesTotal = nImg*nR*nC*1 #since each pixel data is 1 byte
    images_array = 255 - np.asarray(st.unpack('>'+'B'*nBytesTotal, imagesfile.read(nBytesTotal))).reshape((nImg,nR,nC))
    
    labels_array = np.asarray(st.unpack('>'+'B'*nImg, labelsfile.read(nImg))).reshape((nImg,1))
    
    imagesfile.close()
    labelsfile.close()
    
    return images_array, labels_array


features_arrays = getFeaturesArrays(training_data["images"], training_data["labels"])
training_images = features_arrays[0]
training_labels = features_arrays[1]

class Image:
    def __init__(self, arr):
        self.arr = arr
    
    def getPx(self):
        li = []
        for row in range(28):
            for col in range(28):
                li.append(self.arr[row][col])
        
        return li
    
    def distFrom(self, other):
        this_px = self.getPx()
        other_px = other.getPx()
        
        count = 0
        for i in range(0, len(this_px)):
            count += (this_px[i] - other_px[i]) ** 2
        
        return count ** 0.5
    
    def __str__():
        return "An Image of a Digit"

""" SET UP TRAINING DATA """
images = []
features = {}
labelcount = [0] * 10
start = randint(0, len(training_images) - TRAINING_LENGTH)
for i in range(start, start + TRAINING_LENGTH):
    image = Image(training_images[i])
    label = int(training_labels[i])
    labelcount[label] += 1
    images.append(image)
    features[image] = label
#print(labelcount)
print("All " + str(len(images)) + " training images gathered and stored.")

""" SET UP TESTING DATA """
testing_arrays = getFeaturesArrays(testing_data["images"], testing_data["labels"])
testing_imgs_arr = testing_arrays[0]
testing_labels_arr = testing_arrays[1]

testing_images = []
test_dict = {}
for i in range(0, len(testing_imgs_arr)):
    image = Image(testing_imgs_arr[i])
    label = int(testing_labels_arr[i])
    testing_images.append(image)
    test_dict[image] = label

print("All " + str(len(testing_images)) + " testing images gathered and stored.")


""" Define Digit Recognition """
class DigitRecognizer:
    def __init__(self, k):
        self.k = k # k-value for k-nearest neighbors
    
    def merge_sort(self, train_images, dists):
        # Base case - a list of zero or one elements is already sorted
        if len(train_images) <= 1:
            return train_images
    
        # Recursive case
        left = []
        right = []
        for i in range(0, len(train_images)):
            if i < len(train_images) / 2:
                left.append(train_images[i])
            else:
                right.append(train_images[i])
    
        # Recursively sort both sublists
        left = self.merge_sort(left, dists)
        right = self.merge_sort(right, dists)
    
        # Merge the now-sorted sublists
        return self.merge(left, right, dists)
    
    def merge(self, left, right, dists):
        result = []
    
        while len(left) > 0 and len(right) > 0:
            if dists[left[0]] <= dists[right[0]]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
    
        # Either left or right may have elements left; consume them.
        while len(left) > 0:
            result.append(left[0])
            left = left[1:]
        while len(right) > 0:
            result.append(right[0])
            right = right[1:]
        return result
    
    # returns a dictionary that pairs each training image with its distance from test_img
    def distances(self, test_img):
        d = {}
        for image in images:
            d[image] = test_img.distFrom(image)
        return d
    
    def find_nearest_k(self, test_img):
        print("Computing test-digit similarity to training data...")
        d = self.distances(test_img)
        
        print("Finding k-nearest neighbors...")
        train_images = images # preserve images
        sorted_imgs = self.merge_sort(train_images, d)
        
        return sorted_imgs[0:self.k]
    
    # Determine the digit of an image based on the k-nearest neighbors
    # Assume: nearest_k has already been sorted (closest to furthest)
    def best_guess(self, nearest_k):
        labels = []
        for image in nearest_k:
            labels.append(features[image])
        
        #print(labels)
        
        # Create backup label-frequencies list not to be mutated
        label_freqs = [0] * 10
        for label in labels:
            label_freqs[label] += 1
        #print(label_freqs)
        # Create label-frequencies list to be sorted
        sorted_freqs = [0] * 10
        for label in labels:
            sorted_freqs[label] += 1
        sorted_freqs.sort(reverse=True)
        #print(sorted_freqs)
        if len(sorted_freqs) == 1 or sorted_freqs[0] > sorted_freqs[1]:
            return label_freqs.index(sorted_freqs[0])
        #elif sorted_freqs[0] > sorted_freqs[1]:
            #return list(label_freqs).index(sorted_freqs[0])
        
        return self.best_guess(nearest_k[0:len(nearest_k)-1])
    
    def predict_digit(self, image):
        nearest_k = self.find_nearest_k(image)
        print("Making best guess...")
        #print(self.best_guess(nearest_k))
        return self.best_guess(nearest_k)
    
    def correct_answer(self, img):
        return test_dict[img]
    
    # frequency of a number in a list
    def freq(li, num):
        count = 0
        for item in li:
            if num == item:
                count += 1
        return count

def displayDigit(digit):
    px = digit.arr
    px = np.array(px, dtype='float')
    pixels = px.reshape((28, 28))
    plt.imshow(pixels, cmap='gray')
    if digit in features:
        plt.title("Training Digit: " + str(features[digit]))
    if digit in test_dict:
        plt.title("Testing Digit: " + str(test_dict[digit]))
    plt.show()

def displayPrediction(digit):
    displayDigit(digit)
    digit_recognizer = DigitRecognizer(5)
    
    start_time = time.time()
    prediction = digit_recognizer.predict_digit(digit)
    total_time = time.time() - start_time
    answer = digit_recognizer.correct_answer(digit)
    print("Digit Predicted: " + str(prediction))
    print("CORRECT!") if prediction == answer else print("WRONG. Correct Answer: " + str(answer))
    print("It took " + str(round(total_time, 2)) + " seconds to recognize the digit.")
    return (prediction == answer, total_time)
    

def runSimulation(start_i, end_i):
    correct = 0
    total_time = 0
    total_images = 0
    for i in range(start_i, end_i):
        predict = displayPrediction(testing_images[i])
        total_time += predict[1]
        total_images += 1
        if predict[0]:
            correct += 1
        
        print("--------------------------")
        print("Trials Completed:", total_images)
        print("Percent Correct:", round(correct/total_images * 100, 3), "(", correct, "/", total_images, ")")
        print("Average Time:", round(total_time/total_images, 2), "seconds")
        print("--------------------------")
        
runSimulation(0, 50)


