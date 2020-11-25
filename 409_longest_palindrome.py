import collections
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         flag = 0
#         output = 0
#         counter = collections.Counter(s).values()
#         for c in counter:
#             while c >= 2:
#                 output += 2
#                 c -= 2
#             if flag == 0 and c % 2 == 1:
#                 output += 1
#                 flag = 1
            
#         return output

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = sum([(x // 2) * 2 for x in collections.Counter(s).values()])
        return count if count == len(s) else count + 1
        