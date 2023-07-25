# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


""" Before I start

    I would like to know the range of elements if it's equal to or greater than 0
        - According to description, 0 should be ignored.
        - So what if there are 0s in the list nums2?
        - What if there are negative quantities in the lists nums1 and nums2?

    What if m == 0?
        - if m == 0, the answer should be empty array.
    
    I'm wonddering the range of m and n
        - Also, algebraic relationship between them.

"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0: # 0 <= m, n<=200, 1 <= m + n <= 200
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1


""" After I finish
Time complexity : O(1)
    - at most, 'j' in while iteration should be '199'
Space complexity : O(1)
    - no need more spaces than already given spaces for lists.
"""