# one pass
# time: O(n)
# space: O(1)
# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         total = 0
#         runningSum = []
#         for num in nums:
#             total += num
#             runningSum.append(total)
#         return runningSum

# python accumulate
from itertools import accumulate 
class Solution(object):
    def runningSum(self, nums):
        return list(accumulate(nums))

solution = Solution()
print(solution.runningSum([1,2,3,4]))
print(solution.runningSum([1,1,1,1,1]))
print(solution.runningSum([3,1,2,10,1]))
