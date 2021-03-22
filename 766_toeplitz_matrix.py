class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        hashmap = {}
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col-row not in hashmap:
                    hashmap[col-row] = matrix[row][col]
                elif hashmap[col-row] != matrix[row][col]:
                    return False
        return True