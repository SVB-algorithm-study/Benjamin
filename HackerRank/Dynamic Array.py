# https://www.hackerrank.com/challenges/three-month-preparation-kit-dynamic-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=three-month-week-five

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    answer = []
    arr = [[]for _ in range(n)]
    last_answer = 0
    length = len(queries)
    # print(arr)
    
    
    for i in range(length):
        t, x, y = queries[i][0], queries[i][1], queries[i][2]
        print(t,x,y)
        
        idx = (x^last_answer)%n
        if t == 1:
            arr[idx].append(y)
        elif t == 2:
            last_answer = arr[idx][y%len(arr[idx])]
            answer.append(last_answer)
    
    return answer
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
