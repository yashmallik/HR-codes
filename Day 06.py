# #Task
# Given a string,S,N of length n that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Example
# s = abcdef

# Print abc def
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eve = []
odd = []
for i in range(0,n):
    str = input()
    for x in range(0,len(str)):
        if x % 2 == 0:
            eve.append(str[x])
        else:
            odd.append(str[x])
    print("".join(eve)+" "+"".join(odd))
    eve.clear()
    odd.clear()
