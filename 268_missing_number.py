class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        _sum = n * (n + 1) / 2
        return (_sum - sum(nums))


# time: O(nlog(n))
# space: O(1)
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


# time: O(n)
# space: O(n)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        
        for i in range(len(nums)+1):
            if i not in hashset:
                return i