# https://www.hackerrank.com/challenges/three-month-preparation-kit-kangaroo/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    for i in range(1,5001):
        if x1+v1*i == x2+v2*i: return "YES"
        prev_dist = abs((x1+v1*(i-1)) - (x2+v2*(i-1)))
        now_dist = abs((x1+v1*i) - (x2+v2*i))
        # print(prev_dist, now_dist)
        if prev_dist - now_dist <= 0: return "NO"

"""

    de1차원 그래프로 도식화 할 수 있음.
    1. 발산하기 시작하는 순간, 두 그래프는 절대 만날 수 없음.
    2. 평행한 직선은 절대 만날 수 없음.

    x1 = 0, v1 = 2
    x2 = 10000, v2 = 1
    최악의 경우라도 5000번의 연산이면 충분하다. -> 어차피 5000번째 안에 return에 걸림.

    
"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
