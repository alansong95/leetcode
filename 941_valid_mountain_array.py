# brute force
# Time: O(n)
# Space: O(1)
# class Solution:
#     def validMountainArray(self, A):
#         if not A or len(A) < 3 or A[0] > A[1]:
#             return False
#         dir = 1
#         switched = 0
#         prev = A[0]
#         for n in A[1:]:
#             if prev == n:
#                 return False
#             elif dir == 1:
#                 if prev > n and switched:
#                     return False
#                 elif prev >= n and not switched:
#                     switched = 1
#                     dir = -1
#                 prev = n
#             elif dir == -1:
#                 if prev < n:
#                     return False
#                 prev = n
#         return True if switched else False

            
# more readable
class Solution:
    def validMountainArray(self, A):
        N = len(A)
    
        # walk up
        i = 0
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # i == 0: decreasing array
        # i == N - 1: increasing array
        if i == 0 or i == N - 1:
            return False

        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N - 1

solution = Solution()
print(solution.validMountainArray([2,1]))
print(solution.validMountainArray([2,3,3]))
print(solution.validMountainArray([2,3,4]))
print(solution.validMountainArray([0,3,2,1]))
print(solution.validMountainArray([9,8,7,6,5,4,3,2,1,0]))