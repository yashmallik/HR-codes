# #Task
# Given a string,S,N of length n that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Example
# s = abcdef

# Print abc def
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
oStr=[]
eStr = []
for i in range(0,t):
    str=input()
    for x in range(0,len(str)):
        y = float(str[x]) % 2
        if y == 0:
            oStr.append(str[x])
        else:
            eStr.append(str[x])
    print("".join(eStr)+" "+"".join(oStr))
 
