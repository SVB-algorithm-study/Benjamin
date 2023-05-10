#Problem# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
#Solution# https://leetcode.com/problems/find-pivot-index/solutions/3507039/leetcode75-724-find-pivot-index/


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        sum_nums = sum(nums)

        for i in range(len(nums)):
            if result == sum_nums - result - nums[i]: return i
            result += nums[i]
        return -1