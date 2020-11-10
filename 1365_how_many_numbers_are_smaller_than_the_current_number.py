class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        for i, num in enumerate(nums):
            nums[i] = sortedNums.index(num)
        return nums