# # recursive
# class Solution(object):
#     def fib(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         if N == 0 or N == 1:
#             return N
#         else:
#             return self.fib(N - 1) + self.fib(N - 2)

# iterative
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        v1, v2 = 0, 1
        for i in range(N):
            v2, v1 = v1 + v2, v2
        return v1