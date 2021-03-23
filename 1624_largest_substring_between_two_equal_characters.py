class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = collections.defaultdict(list)
        for i, c in enumerate(s):
            ht[c].append(i)
            
        res = 0
        for k, v in ht.items():
            diff = v[-1] - v[0]
            if diff > res:
                res = diff
        return res - 1