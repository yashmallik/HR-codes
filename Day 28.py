#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    sheet = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        email = re.findall("@gmail.com$", emailID)
        if(email):
            sheet.append(firstName)
    sheet = sorted(sheet)
    
    for n in sheet:
        print(n)
