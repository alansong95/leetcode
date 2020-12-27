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
# class Solution(object):
#     def fib(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         v1, v2 = 0, 1
#         for _ in range(N):
#             v2, v1 = v1 + v2, v2
#         return v1

# just recursion
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        
        return self.fib(n-1) + self.fib(n-2)

# recursion + memoization (top down dp)
class Solution2(object):
    def fib(self, n):
        return self.fibHelper(n, {})
    
    def fibHelper(self, n, memo):
        if n < 2:
            return n
        
        if n in memo:
            return memo[n]

        memo[n] = self.fibHelper(n-1, memo) + self.fibHelper(n-2, memo)
        return memo[n]

# bottom up dynamic programming (forward)
class Solution3(object):
    def fib(self, n):
        if n < 2:
            return n
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

# bottom up dynamic programming (backward)
class Solution4(object):
    def fib(self, n):
        if n < 2:
            return n
        
        dp = [0] * (n+2)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n):
            dp[i+1] += dp[i]
            dp[i+2] += dp[i]
        return dp[n]