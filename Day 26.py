# Objective
# Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing.

# Task
# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

# If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0.)
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 X (no of due date).
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 X (no of due month) .
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of 500 HACKOS.

-------------------------------X--------------------------------X-----------------------------------------X--------------------------------------------------------------X---------------------------X----------------------------------
-------------------------------X--------------------------------X-----------------------------------------X--------------------------------------------------------------X---------------------------X--------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
def bookDue(actual, expected):
    
    if actual[2] == expected[2]:
        if actual[1] == expected[1]:
            if actual[0] > expected[0]:
                late = actual[0] - expected[0]
                fine = 15*late
                print(fine)
            else:
                print(0)
        elif actual[1] > expected[1]:
            late = actual[1]-expected[1]
            fine = 500*late
            print(fine)
        else:
            print(0)
    elif actual[2] > expected[2]:
        print(10000)
    else:
        print(0)


actual  = input().split(" ")
expected = input().split(" ")
for i in range(3):
    actual[i] = int(actual[i])
    expected[i] = int(expected[i])

bookDue(actual, expected)
