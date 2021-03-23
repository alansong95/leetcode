class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = [0]
        
        for g in gain:
            altitude.append(altitude[-1] + g)
        return max(altitude)