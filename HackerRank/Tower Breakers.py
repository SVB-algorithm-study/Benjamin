# https://www.hackerrank.com/challenges/three-month-preparation-kit-tower-breakers-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def count_common_divisor(m):
    cnt = 0
    end = int(m**0.5 + 1)
    for i in range(1,end):
        if m%i == 0:
            cnt+=2
    if (end-1)**2 == m:
        cnt -= 1
    return cnt

def is_prime(m):
    if m < 2:
        return False
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0: return False
    return True
        
def towerBreakers(n, m):
    # Write your code here
    # print(count_common_divisor(1), count_common_divisor(17), count_common_divisor(25))
    # if n==1: return 1
    
    # if n % 2 and count_common_divisor(m) % 2: # n: odd, m:odd
    #     return 2
    # elif n % 2 and count_common_divisor(m) % 2 + 1: # n: odd, m: even
    #     return 1
    # elif n % 2 + 1 and count_common_divisor(m) % 2: # n: even, m: odd
    #     return 1
    # elif n % 2 + 1 and count_common_divisor(m) %2 + 1: # n: even, m: even
    #     return 2

    if m == 1: return 2
    # if n == 1: return 1
    
    # if is_prime(m):
    #     return 1 if n % 2 else 2
    # else:
    #     return n % 2 + 1

    return 1 if n % 2 else 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
