# https://www.hackerrank.com/challenges/three-month-preparation-kit-separate-the-numbers/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    
    for i in range(1,len(s)//2+1):
        start = int(s[:i])
        temp = [start]
        while len(''.join(map(str,temp))) < len(s):
            temp.append(temp[-1]+1)
        if s == ''.join(map(str,temp)):
            print("YES", start)
            return 0
    print("NO")
    
        

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
