# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         splited = s.split(' ')
#         for i in range(len(splited)):
#             splited[i] = splited[i][::-1]
#         return ' '.join(splited)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splited = [w[::-1] for w in s.split(' ')]
        return ' '.join(splited)