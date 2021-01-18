class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ht = {}
        res = 0
        for num in nums:
            if k - num in ht and ht[k - num] > 0:
                ht[k - num] -= 1
                res += 1
            else:
                ht[num] = ht.get(num, 0) + 1
        return res