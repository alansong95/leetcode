class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = {}
        res = 0
        
        for num in nums:
            ht[num] = ht.get(num, 0) + 1
        
        for num in ht:
            if num+1 in ht:
                res = max(res, ht[num] + ht[num+1])
        return res
            
        
            
        
        