class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        i = 0
        j = 0
        count = 0
        while i < len(matrix) and i < len(matrix[0]):
            while i + j <= count:
                ans.append(matrix[i][j])
                

solution = Solution()
print(solution.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
))