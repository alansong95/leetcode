class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        memo = {}
        
        def helper(i, j):
            if i == 0 or j == 0 or i == j:
                return 1
            elif (i, j) in memo:
                return memo[(i, j)]
            else:
                memo[(i, j)] = helper(i-1, j-1) + helper(i-1, j)
                return memo[(i, j)]
        
        res = []
        for i in range(rowIndex+1):
            res.append(helper(rowIndex, i))
        return res