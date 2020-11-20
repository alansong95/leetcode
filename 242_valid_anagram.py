import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counterS = collections.Counter(s)
        counterT = collections.Counter(t)
        return len((counterS - counterT).keys()) == 0 and len((counterT - counterS).keys()) == 0