#problem# https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=study-plan&id=level-1
#solution# https://leetcode.com/problems/running-sum-of-1d-array/solutions/3507217/1480-running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [0]
        for i in range(len(nums)):
            answer.append(answer[-1]+nums[i])
        return answer[1:]