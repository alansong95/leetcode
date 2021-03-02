class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binarySearch(row, target):
            l, r = 0, len(row) -1
            while l <= r:
                mid = (l + r) / 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        for row in matrix:
            if binarySearch(row, target):
                return True
        return False


# divide and conquer 
class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        def search(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right-left) // 2
            
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search(left, row, mid-1, down) or \
                    search(mid + 1, up, right, row-1)
        return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)