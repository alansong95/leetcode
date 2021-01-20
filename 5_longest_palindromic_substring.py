class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s) - 1, -1, -1):
            for j in range(0, len(s) - i):
                if self.isPalindrome(s[j:i+j+1]):
                    return s[j:i+j+1]
        
    
    def isPalindrome(self, s):
        return s == s[::-1]