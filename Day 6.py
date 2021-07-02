# #Task
# Given a string,S,N of length n that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Example
s = abcdef

# Print abc def
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in (0,t):
    str=input()
    print(str[0::2]+" "+str[1::2])
