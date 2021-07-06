# Objective
# Today, we are building on our knowledge of arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video.

# Context
# Given a 6*6 2D A Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    rev = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for z in range(4):
           rev.append(arr[i][z]+arr[i][z+1]+arr[i][z+2]+arr[i+1][z+1]+arr[i+2][z]+arr[i+2][z+1]+arr[i+2][z+2])
    print(max(rev))
