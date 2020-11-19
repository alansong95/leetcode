class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        
        l = 0
        r = len(S) - 1
        
        while l < r:
            while not S[l].isalpha():
                l += 1
            while not S[r].isalpha():
                r -= 1
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        
        return ''.join(S)