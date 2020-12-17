class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        diff = False
        
        while l < r:
            if s[l] != s[r]:
                if not diff and (l+1 >= r or s[l+1] == s[r]) and (l+2 >= r-1 or s[l+2] == s[r-1]):
                    l += 1
                elif not diff and (l >= r-1 or s[l] == s[r-1]) and (l+1 >= r-2 or s[l+1] == s[r-2]):
                    r -= 1
                else:
                    return False
                diff = True
            l += 1
            r -= 1
        return True
                
        