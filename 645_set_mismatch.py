class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums) - sum(set(nums)), len(nums) * (len(nums) + 1) / 2 - sum(set(nums))]


class Solution2(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                duplicate = num
        
        for i in range(1, len(nums)+1):
            if i not in hashset:
                missing = i
                break
        
        return [duplicate, missing]