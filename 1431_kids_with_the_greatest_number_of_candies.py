class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        _max = max(candies)
        return map(lambda x: x + extraCandies >= _max, candies)