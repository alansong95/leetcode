# time: O(n^3)
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

# time: O(n^2)
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        ans = ''
        for i in range(n):
            dp[i][i] = True
        ans = s[0]
        
        maxLen = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if maxLen < j - i + 1:
                            maxLen = j - i + 1
                            ans = s[i:j+1]
        return ans
                