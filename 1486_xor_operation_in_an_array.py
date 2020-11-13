# two passes and a list
# time: O(n)
# space: O(n)
# class Solution(object):
#     def xorOperation(self, n, start):
#         """
#         :type n: int
#         :type start: int
#         :rtype: int
#         """
#         nums = []
#         for i in range(n):
#             nums.append(start + 2*i)
        
#         xored = nums[0]
#         for num in nums[1:]:
#             xored = xored ^ num
#         return xored
        
# one pass and no list
# time: O(n)
# space: O(1)
class Solution(object):
    def xorOperation(self, n, start):
        xored = start
        for i in range(1, n):
            xored = xored ^ (start + 2*i)
        return xored
        