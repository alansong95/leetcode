# Brute force
# Time: O(nlogn)
# Space: 1
# class Solution(object):
#     def sortedSquares(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         for i in range(len(A)):
#             A[i] = A[i] * A[i]
#         return sorted(A)

# one line solution
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # for i in range(len(A)):
        #     A[i] = A[i] * A[i]
        # return sorted(A)
        return sorted([x * x for x in A])

solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))
print(solution.sortedSquares([-7,-3,2,3,11]))