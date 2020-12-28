# class Solution(object):
#     def halvesAreAlike(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         a, b = s[0:len(s)/2], s[len(s)/2:]
#         count1 = count2 = 0
#         for (a1, b1) in zip(a, b):
#             if a1 in vowels:
#                 count1 += 1
#             if b1 in vowels:
#                 count2 += 1
#         return count1 == count2
        
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        for i in range(len(s)/2):
            if s[i] in vowels:
                count += 1
        for i in range(len(s)/2, len(s)):
            if s[i] in vowels:
                count -= 1
        return count == 0
        
        