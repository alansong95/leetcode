class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        ht = {x[0]: x for x in pieces}
        res = []
        
        for num in arr:
            res += ht.get(num, [])
            
        return res == arr