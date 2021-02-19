class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0] * len(A)
        _sum = 0
        
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1 + dp[i-1]
                _sum += dp[i]
        return _sum