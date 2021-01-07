class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1, arr[0]):
            k -= 1
            if k == 0:
                return i
        
        for i, missing in enumerate(arr[:-1]):
            while missing + 1 != arr[i+1]:
                missing += 1
                k -= 1
                if k == 0:
                    return missing
                
        return arr[-1] + k