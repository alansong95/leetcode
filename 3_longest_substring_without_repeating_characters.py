class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        seen = {}
        l = 0
        longest = 0
        
        for i in range(len(s)):
            if s[i] not in seen or seen[s[i]] < l:
                seen[s[i]] = i
            else:
                longest = max(longest, i-l)
                l = seen[s[i]] + 1
                seen[s[i]] = i
                
        return max(longest, len(s)-l)