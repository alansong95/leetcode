class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        i = 0
        j = len(mat[0]) - 1
        _sum = 0    
        
        while i < len(mat[0]):
            if i != j:
                _sum += mat[i][i]
            _sum += mat[i][j]
            i += 1
            j -= 1
        return _sum