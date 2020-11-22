class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ht_p = {}
        ht_s = {}
        words = s.split(' ')
        
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c in ht_p and ht_p[c] != w:
                return False
            elif w in ht_s and ht_s[w] != c:
                return False
            ht_p[c] = w
            ht_s[w] = c
        return True