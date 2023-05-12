# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan&id=level-1

from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s: return True
        q = deque(s)

        for c in t:
            if q[0] == c:
                q.popleft()

            if not q:
                return True

        return False