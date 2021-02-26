class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        
        l = 0
        while l < len(nums) and nums[l] == nums_sorted[l]:
            l += 1
        
        if l == len(nums):
            return 0
        
        r = len(nums) - 1
        while nums[r] == nums_sorted[r]:
            r -= 1
            
        return r - l + 1