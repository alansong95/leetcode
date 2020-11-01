class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                mp += (prices[i] - prices[i-1])
        return mp

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]) == 7)
print(solution.maxProfit([1,2,3,4,5]) == 4)
print(solution.maxProfit([7,6,4,3,1]) == 0)
print(solution.maxProfit([]) == 0)
