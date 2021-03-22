class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = ''.join([c for c in s if c.isdigit()])
        nums = sorted(set(nums))
        
        if len(nums) > 1:
            return nums[-2]
        return -1
        