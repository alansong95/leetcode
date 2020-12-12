class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        s = s[::-1]
        res = '.'.join(s[i:i+3] for i in range(0, len(s), 3))
        return res[::-1]