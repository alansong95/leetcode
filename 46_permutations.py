class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(curr, left):
            if len(curr) == n:
                res.append(curr[:])
            for i in range(len(left)):
                backtrack(curr + [left[i]], left[:i] + left[i+1:])
    
        n = len(nums)
        res = []
        backtrack([], nums)
        return res
