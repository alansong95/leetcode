# brute force
# time: O(n^2)
# space: O(1)
# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#         return count

# hash table
# time: O(n)
# space: O(n)
# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         ht = {}
#         for i, num in enumerate(nums):
#             if num in ht:
#                 ht[num] += 1
#             else:
#                 ht[num] = 1
        
#         _values = ht.values()
#         for value in _values:
#             count += (value*(value-1))/2
#         return count

import collections

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return(sum(x*(x-1) / 2 for x in collections.Counter(nums).values()))
        
        