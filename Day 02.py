# Objective
# In this challenge, you will work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total_tip = (meal_cost*tip_percent/100);
    total_tax = (meal_cost*tax_percent/100);
    return print(round(meal_cost+total_tip+total_tax));
        
        
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
