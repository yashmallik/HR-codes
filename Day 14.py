# Objective
# Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!

# The absolute difference between two integers, a and b, is written as |a-b| . The maximum absolute difference between two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in __elements.

# The Difference class is started for you in the editor. It has a private integer array (elements) for storing N non-negative integers, and a public integer (maximumDifference) for storing the maximum absolute difference.

# Task
# Complete the Difference class by writing the following:

# A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
# A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifference instance variable.


class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    maximumDifference = 0
    def computeDifference(self):
        minn = min(self.__elements)
        maxx = max(self.__elements)
        self.maximumDifference = maxx - minn
            
            
                

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
