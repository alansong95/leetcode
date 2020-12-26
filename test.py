def combinatorial(self, m, n):
    dp = [[0 for i in range(n)] for j in range(m)]

    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]:
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
    
    return dp[m-1][n-1]


def blocked(self, blocked):
    m = len(blocked)
    n = len(blocked[0])
    dp = [[0 for i in range(n)] for j in range(m)]

    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if blocked[i][j] == 1:
                dp[i][j] = 0
            elif i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]:
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
    
    return dp[m-1][n-1]


def maxCoin(self, coins):
    m = len(coins)
    n = len(coins[0])
    dp = [[0 for i in range(n)] for j in range(m)]


    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + coins[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + coins[i][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1] + coins[i][j]
    
    return dp[m-1][n-1]