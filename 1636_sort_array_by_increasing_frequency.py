class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        counter_lst = counter.items()
        counter_lst.sort(key=lambda x: (x[1], -x[0]))
        res = [[v] * f for v, f in counter_lst]
        return sum(res, [])