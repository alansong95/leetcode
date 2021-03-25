class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        count = 0
        i = 0
        while i + m < len(arr):
            if arr[i] != arr[i+m]:
                count = 0
            count += (arr[i] == arr[i+m])
            if count == (k-1)*m:
                return True
            i += 1
        return False