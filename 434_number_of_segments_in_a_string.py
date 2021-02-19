class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        raw = s.split(' ')
        filtered = filter(lambda c: c != '', raw)
        return len(filtered)

class Solution2(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(filter(lambda c: c != '', s.split(' ')))