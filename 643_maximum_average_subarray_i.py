class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        _max = sum(nums[0:k])
        temp = _max
        for i in range(len(nums) - k):
            temp = temp - nums[i] + nums[i+k]
            _max = max(temp, _max)
        return _max/float(k)