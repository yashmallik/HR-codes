Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given set S={1,2,3,4,5.......N}. Find two integers, A and B (where A<B), from set S such that the value of A&B is the maximum possible and
also less than a given integer, K. In this case, & represents the bitwise AND operator.

Function Description
Complete the bitwiseAnd function in the editor below.

bitwiseAnd has the following paramter(s):
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive

----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X
----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X
def bitwiseAnd(N, K):
    # Write your code here
    checker = 0
    for A in range(1,K):
        for B in range(A+1,N+1):
                x = A&B
                if checker<x and x<K:
                    checker = x
    return checker
