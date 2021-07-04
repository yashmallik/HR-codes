# Objective
# Today, we are learning about an algorithmic concept called recursion. Check out the Tutorial tab for learning materials and an instructional video.

# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.

# factorial has the following paramter:

# int n: an integer
# Returns

# int: the factorial of n

#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n* factorial(n-1)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

