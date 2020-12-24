class Solution(object):
    def minCostClimbingStairs(self, p):
        """
        :type cost: List[int]
        :rtype: int
        """
        p = p + [0]
        n = len(p)
        dp = [0] * n
        dp[0] = p[0]
        dp[1] = p[1]
        
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + p[i]
        print dp
        return dp[n-1]