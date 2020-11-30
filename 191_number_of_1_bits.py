# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         count = 0
#         while n > 0:
#             if n % 2 == 1:
#                 count += 1
#             n = n // 2
#         return count

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n)[2:].count('1')