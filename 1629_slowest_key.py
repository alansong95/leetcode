class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        temp = [releaseTimes[0]] + [y - x for x, y in zip(releaseTimes, releaseTimes[1:])]
        _max = max(temp)
        return max([keysPressed[i] for i, val in enumerate(temp) if val == _max])