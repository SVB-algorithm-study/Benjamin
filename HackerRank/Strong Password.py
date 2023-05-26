# https://www.hackerrank.com/challenges/three-month-preparation-kit-strong-password/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=three-month-week-five

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    cnt = 0
    flag = [True] * 4
    
    for c in password:
        if flag[0] and c in numbers:
            flag[0] = False
        elif flag[1] and c in lower_case:
            flag[1] = False
        elif flag[2] and c in upper_case:
            flag[2] = False
        elif flag[3] and c in special_characters:
            flag[3] = False
    
    res = sum(flag)
    
    return res if n>6 else max(res,6-n)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
