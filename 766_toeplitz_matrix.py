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


class Solution2(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(len(matrix)-1):
            for col in range(len(matrix[row])-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True