class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_set = sum(set(nums))
        sum_real = len(nums) * (len(nums) + 1) / 2
        missing = sum_real - sum_set
        
        return [sum(nums) + missing - sum_real, missing]