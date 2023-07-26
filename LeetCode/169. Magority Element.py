""" Before
    What is the range of elements?
    What is the range of n?
    
    I can use O(n) sol iterating all of the list.

"""

""" Solution1: Fail - Memery Limit Exceeded
class Solution: # Memory Limit Exceeded
    def majorityElement(self, nums: List[int]) -> int:
        count_list = [0 for _ in range(2*10**9+1)]
        for e in nums:
            count_list[e+10**9] += 1
        
        return max(count_list)
"""

""" Review1
    The count_list size is too large.
    Let't use Counter module.
"""

""" Solution2: Accepted - Using Counter Module
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        return Counter(nums).most_common(1)[0][0]
"""

""" Review2
    Time complexity: O(n)
    Can I evaluate the Counter method?
"""

class Solution: # Solution 3
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1

        return max(count_dict, key=count_dict.get)
        
""" Review 3
    max에서 key를 사용하는 주된 목적은 index(key)와 value 짝의 튜플형태로 이루어진 리스트에서 key와 value 중에 어떤것을 기준으로 max값을 구할지 선택하기위한 목적으로 많이 활용된다.
    🔥 max의 key : 함수로 구현되어있고, lambda함수로 작성해도 상관없다.
    Time complexity: O(n)
"""