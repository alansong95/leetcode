class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [int(x) for x in str(n)]
        return reduce(lambda x, y: x * y, arr) - sum(arr)