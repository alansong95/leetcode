class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1]
        
        for i in range(2, n+1):
            if i % 2 == 0:
                nums.append(nums[i/2])
            else:
                nums.append(nums[i//2] + nums[i//2 + 1])
        return max(nums[:n+1])


class Solution2(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1]
        _max = 0 if n == 0 else 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                nums.append(nums[i/2])
            else:
                nums.append(nums[i//2] + nums[i//2 + 1])
            _max = max(_max, nums[-1])
        return _max