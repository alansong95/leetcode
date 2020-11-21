class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ht = {}
        while n != 1:
            n = self.sumOfSquaresOfDigits(n)
            if n in ht:
                return False
            ht[n] = n
        return True
    
    def sumOfSquaresOfDigits(self, n):
        output = 0
        while n > 0:
            output += ((n % 10) * (n % 10))
            n = n // 10
        return output