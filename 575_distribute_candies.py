class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        hashset = set(candyType)
        return min(len(hashset), len(candyType) / 2)