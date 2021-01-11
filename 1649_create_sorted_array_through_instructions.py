from sortedcontainers import SortedList

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        sl = SortedList()
        cost = 0
        MOD = 10 ** 9 + 7
        
        for n in instructions:
            left = sl.bisect_left(n)
            right = len(sl) - sl.bisect_right(n)
            
            cost += min(left, right)
            cost %= MOD
            sl.add(n)
        return cost