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

    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + coins[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + coins[i][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1] + coins[i][j]
    
    return dp[m-1][n-1]


def minCoinPath(self, coins):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
    return self.getPath(dp, m-1, n-1, [])

def getPath(self, dp, i, j, path):
    if i == 0 and j == 0:
        path.append((i, j))
        return path
    elif i == 0:
        path = self.getPath(dp, i, j-1, path)
    elif j == 0:
        path = self.getPath(dp, i-1, j, path)
    else:
        if dp[i-1][j] < dp[i][j-1]:
            path = self.getPath(dp, i-1, j, path)
        else:
            path = self.getPath(dp, i, j-1, path)
    path.append((i, j))
    return path


# paint fence with two colors
def numWays(n):
    dp = [[0 for _ in range(2)] for _ in range(n-1)]

    # green = 1, blue = 0
    dp[1][0] = 1
    dp[1][1] = 1
    dp[2][0] = 2 # 10, 00
    dp[2][1] = 2 # 01, 11

    for i in range(3, n+1):
        for j in range(2):
            dp[i][j] = dp[i-1][1-j] + dp[i-2][1-j]
    
    return dp[n][0] + dp[n][1]

# fibonacci
# recursion
def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# recursion + memoization (top down dp)
def fibTopDown(n):
    return fibTopDownHelper(n, {})

def fibTopDownHelper(n, memo):
    if n < 2:
        return n
    
    if n in memo:
        return memo[n]

    memo[n] = self.fibHelper(n-1, memo) + self.fibHelper(n-2, memo)
    return memo[n]

# bottom up dynamic programming (forward)
def fibBottomUpDPForward(n):
    if n < 2:
        return n
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# bottom up dynamic programming (backward)
def fibBottomUpDPBackward(n):
    if n < 2:
        return n
    
    dp = [0] * (n+2)
    dp[0] = 0
    dp[1] = 1
    for i in range(1, n):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
    return dp[n]