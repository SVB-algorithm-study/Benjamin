# https://leetcode.com/problems/longest-palindrome/description/?envType=study-plan&id=level-1

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_of = Counter(s)
        oddCount = 0

        for value in count_of.values():
            if value % 2:
                oddCount += 1
        
        return len(s) - oddCount + 1 if oddCount else len(s)