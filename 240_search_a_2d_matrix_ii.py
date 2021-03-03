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
        
        def helper(left, right, top, bottom):
            if left > right or top > bottom:
                return False
            if matrix[top][left] > target or matrix[bottom][right] < target:
                return False
            
            mid = (left + right) // 2
            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return helper(left, mid-1, row, bottom) or \
                    helper(mid+1, right, top, row-1)
        return helper(0, len(matrix[0])-1, 0, len(matrix)-1)