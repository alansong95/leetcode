class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def getAverage(M, row, col):
            _sum = 0
            count = 0
            for i in [-1, 0, 1]:
                if i + row >= 0 and i + row < len(M):
                    for j in [-1, 0, 1]:
                        if j + col >= 0 and j + col < len(M[i]):
                            _sum += M[i+row][j+col]
                            count += 1
            return _sum // count
                    
        
        new_M = [[0] * len(M[0]) for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[i])):
                new_M[i][j] = getAverage(M, i, j)
        return new_M