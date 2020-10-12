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
# Time: O(nlogn)
# Space: n
# class Solution(object):
#     def sortedSquares(self, A):
#         return sorted([x * x for x in A])

# linear solution
# Time: O(n)
# Space: O(n)
class Solution(object):
    def sortedSquares(self, A):
        ans = [0] * len(A)

        left = 0
        right = len(A) - 1

        for i in range(len(ans)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                ans[i] = A[left] * A[left]
                left += 1
            else:
                ans[i] = A[right] * A[right]
                right -= 1
        return ans



solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))
print(solution.sortedSquares([-7,-3,2,3,11]))