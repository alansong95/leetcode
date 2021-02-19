class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        _list = list(s)
        
        for i in range(0, len(s), 2*k):
            _list[i:i+k] = reversed(_list[i:i+k])
        return ''.join(_list)