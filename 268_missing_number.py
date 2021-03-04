class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        _sum = n * (n + 1) / 2
        return (_sum - sum(nums))


# O(nlog(n))
class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
            