class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ht = {}
        for ind, num in enumerate(nums):
            if num in ht:
                if ind - ht[num] <= k:
                    return True
                else:
                    ht[num] = ind
            else:
                ht[num] = ind
        return False