# 

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    
    length = len(s)
    if length % 2: return -1

    answer = 0
    count = [0]*26

    formal = s[:length//2]
    latter = s[length//2:]
    
    for i in range(length//2):
        count[ord(formal[i])-ord('a')] += 1
        count[ord(latter[i])-ord('a')] -= 1
    
    for c in count:
        answer += abs(c)
    
    return answer//2
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
