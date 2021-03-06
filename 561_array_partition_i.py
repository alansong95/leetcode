class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums_sorted[i]
        return res