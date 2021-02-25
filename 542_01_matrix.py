class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        nr = len(matrix)
        nc = len(matrix[0])
        
        for r in range(nr):
            for c in range(nc):
                if matrix[r][c] == 1:
                    queue = [(r, c, 0)]
                    while queue:
                        row, col, distance = queue.pop(0)
                        
                        if row-1 >= 0:
                            if matrix[row-1][col] == 0:
                                matrix[r][c] = distance + 1
                                break
                            else:
                                queue.append((row-1, col, distance+1))
                            
                        if row+1 < nr:
                            if matrix[row+1][col] == 0:
                                matrix[r][c] = distance + 1
                                break
                            else:
                                queue.append((row+1, col, distance+1))
                                
                        if col-1 >= 0:
                            if matrix[row][col-1] == 0:
                                matrix[r][c] = distance + 1
                                break
                            else:
                                queue.append((row, col-1, distance+1))

                        if col+1 < nc:
                            if matrix[row][col+1] == 0:
                                matrix[r][c] = distance + 1
                                break
                            else:
                                queue.append((row, col+1, distance+1))                                
                                
        return matrix