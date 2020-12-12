class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        rev_vowels = [c for c in s[::-1] if c in vowels]
        
        rev_i = 0
        for i, c in enumerate(s):
            if c in vowels:
                s[i] = rev_vowels[rev_i]
                rev_i += 1
        return ''.join(s)
        
        