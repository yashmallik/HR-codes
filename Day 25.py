# Objective
# Today we will learn about running time, also known as time complexity. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it is  or .

# Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

# Input Format

# The first line contains an integer, , the number of test cases.
# Each of the  subsequent lines contains an integer, , to be tested for primality.

__________________________________________________________________________________________________________________________________________________________________________________________

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
round = int(input())
for j in range(round):
    num = int(input())
    numSqr = math.floor(math.sqrt(num))
    count = 0
    for i in range(2,1+numSqr):
    
        if num%i==0:
            print("Not prime")
            count += 1
            break
    if num <=1:
        print("Not prime")
    elif count == 0:
        print("Prime")

    
