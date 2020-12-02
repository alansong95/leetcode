class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        res = 0
        for s, e in zip(startTime, endTime):
            if queryTime >= s and queryTime <= e:
                res += 1
        return res
        