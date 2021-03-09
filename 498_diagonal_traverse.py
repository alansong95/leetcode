class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        hashtable = [[] for i in range(2*max(len(matrix), len(matrix[0]))-1)]
        
        # populate hashtable
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                hashtable[row+col].append(matrix[row][col])
        
        
        # populate answer
        res = []
        flip = True
        for e in hashtable:
            if flip:
                e.reverse()
            res += e
            flip = not flip
        
        return res