class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res = []
        
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    res.append(prices[i] - prices[j])
                    break
                if j == len(prices) - 1:
                    res.append(prices[i])
                j += 1
        return res + [prices[-1]]