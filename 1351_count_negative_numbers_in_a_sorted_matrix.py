# class Solution(object):
#     def countNegatives(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         count = 0
        
#         for i in range(len(grid)):
#             j = len(grid[i]) - 1
#             while j >= 0 and grid[i][j] < 0:
#                 count += 1
#                 j -= 1
#         return count

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][len(grid[i])-j-1] < 0:
                    count += 1
        return count