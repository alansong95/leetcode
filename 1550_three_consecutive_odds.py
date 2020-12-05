class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for n in arr:
            if n % 2 == 1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False