# brute force
# time: O(n^2)
# space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > mp:
                    mp = prices[j] - prices[i]
        return mp

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
