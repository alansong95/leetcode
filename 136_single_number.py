# hash table
# time: O(n)
# space: O(n)
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         table = {}
#         for num in nums:
#             if num not in table:
#                 table[num] = 1
#             else:
#                 del table[num]
#         return table.keys()[0]

# use sets
# time: O(n)
# space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)