def climbStairs(self, m, n):
    dp = [[0 for i in range(n)] for j in range(m)]

    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]:
            else if i > 0:
                dp[i][j] = dp[i-1][j]
            else if j > 0:
                dp[i][j] = dp[i][j-1]
    
    return dp[m-1][n-1]