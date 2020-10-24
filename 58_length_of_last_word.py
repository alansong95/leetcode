# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s.split()) == 0:
#             return 0
#         return len(s.split()[-1])

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = len(s)-1
        
        while p >= 0 and s[p] == ' ':
            p -= 1
        
        count = 0
        while p >= 0 and s[p] != ' ':
            count += 1
            p -= 1
        return count
        