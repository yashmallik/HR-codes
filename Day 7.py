# Objective
# Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.
# Task
# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

# Example
# A =[1,2,3,4]


# Print 4 3 2 1. Each integer is separated by one space.



#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(" ".join(str(e) for e in reversed(arr)))

        
        
