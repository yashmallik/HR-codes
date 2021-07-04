# Objective
# Today, we/'re learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
dic = {}
for i in range(0,t):
    d = input()
    d = d.split(" ")    
    dic[d[0]] = d[1]

for x in range(0,t):
    try:
        c = input()
        n = dic.get(c)
        if n != None:
            print("{}={}".format(c,n))
        else:
            print("Not found")
    except:
        break
