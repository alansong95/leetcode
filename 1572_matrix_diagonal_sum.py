class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        k = 0
        i = 0
        j = len(mat[0]) - 1
        
        _sum = 0
        
        while j >= 0:
            if i != j:
                _sum += mat[k][i]
            _sum += mat[k][j]
            i += 1
            j -= 1
            k += 1
        return _sum