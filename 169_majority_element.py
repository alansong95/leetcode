# hash table
# time: O(n)
# space: O(n)
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         ht = {}
#         for num in nums:
#             if num not in ht:
#                 ht[num] = 1
#             else:
#                 ht[num] += 1
#         for num in ht:
#             if ht[num] > len(nums) // 2:
#                 return num

# hash table in 2 lines
# time: O(n)
# space: O(n)
import collections
class Solution(object):
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts, key=counts.get)

solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2,1,1,1,2,2]))
