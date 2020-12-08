class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {}
        
        for n in sorted(set(arr)):
            rank[n] = len(rank) + 1
        
        return list(map(lambda n: rank[n], arr))