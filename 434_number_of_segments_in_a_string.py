class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        raw = s.split(' ')
        filtered = filter(lambda c: c != '', raw)
        return len(filtered)