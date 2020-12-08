# class Solution(object):
#     def slowestKey(self, releaseTimes, keysPressed):
#         """
#         :type releaseTimes: List[int]
#         :type keysPressed: str
#         :rtype: str
#         """
#         temp = [releaseTimes[0]] + [y - x for x, y in zip(releaseTimes, releaseTimes[1:])]
#         _max = max(temp)
#         return max([keysPressed[i] for i, val in enumerate(temp) if val == _max])

class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_time = releaseTimes[0]
        max_index = 0
        
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff > max_time:
                max_time = diff
                max_index = i
            elif diff == max_time and keysPressed[i] > keysPressed[max_index]:
                max_index = i
        
        
        return keysPressed[max_index]
                