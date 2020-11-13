class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        
        xored = nums[0]
        for num in nums[1:]:
            xored = xored ^ num
        return xored
        