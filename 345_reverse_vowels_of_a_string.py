# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         vowels =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         s = list(s)
#         rev_vowels = [c for c in s[::-1] if c in vowels]
        
#         rev_i = 0
#         for i, c in enumerate(s):
#             if c in vowels:
#                 s[i] = rev_vowels[rev_i]
#                 rev_i += 1
#         return ''.join(s)
        
        
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in vowels: l += 1
            while l < r and s[r] not in vowels: r -= 1
            if l > r: break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r -1
        return ''.join(s)
        