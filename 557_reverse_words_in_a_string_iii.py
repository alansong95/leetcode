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

# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         splited = [w[::-1] for w in s.split(' ')]
#         return ' '.join(splited)

# without split and join
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ''
        word = ''
        for c in s:
            if c == ' ':
                output = output + word[::-1] + ' '
                word = ''
            else:
                word += c
        return output + word[::-1]