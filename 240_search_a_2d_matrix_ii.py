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