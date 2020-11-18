import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counter = collections.Counter(moves)
        return counter.get('U') == counter.get('D') and counter.get('R') == counter.get('L')