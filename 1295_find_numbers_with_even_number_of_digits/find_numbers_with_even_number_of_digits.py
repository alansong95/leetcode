# Time: O(n)
# Space: O(1)
# class Solution(object):
#     def findNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         for num in nums:
#             if self.isEvenNumOfDigits(num):
#                 count += 1
#         return count

#     def isEvenNumOfDigits(self, num):
#         count = 0
#         while num > 0:
#             num = num // 10
#             count += 1
#         return count % 2 == 0

class Solution(object):
    def findNumbers(self, nums):
        return len([x for x in nums if len(str(x)) % 2 == 0])

solution = Solution()
print(solution.findNumbers([12,345,2,6,7896]))
print(solution.findNumbers([555,901,482,1771]))
print(solution.findNumbers([10]))
print(solution.findNumbers([2]))