# two lists 
# Time: O(n)
# Space: O(n)
# class Solution(object):
#     def sortArrayByParity(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         even = [x for x in A if x % 2 == 0]
#         odd = [x for x in A if x % 2 == 1]
#         return even + odd

# in place
class Solution(object):
    def sortArrayByParity(self, A):
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
            else:
                if A[j] % 2 == 1:
                    j -= 1
                else:
                    A[j], A[i] = A[i], A[j]
                    i += 1
                    j -= 1
        return A


solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))