class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        longest = 0
        streak = 0
        nums = nums + [-float('inf')]
        
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                streak += 1
            else:
                longest = max(longest, streak)
                streak = 0
        return max(longest, streak) + 1