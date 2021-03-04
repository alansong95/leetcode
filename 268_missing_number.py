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
class Solution3(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        
        for i in range(len(nums)+1):
            if i not in hashset:
                return i


# time: O(n)
# space: O(n)
import collections
class Solution4(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c1 = collections.Counter(nums)
        c2 = collections.Counter(range(len(nums)+1))
        return (c2 - c1).elements().next()


# time: O(n)
# space: O(1)
class Solution5(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)