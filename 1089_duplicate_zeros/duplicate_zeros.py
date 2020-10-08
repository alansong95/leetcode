# if constraint "in place" is not there
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        dest = []
        for e in arr:
            dest.append(e)
            if e == 0:
                dest.append(e)
        arr = dest[:len(arr)]
        print(arr)
            
            




solution = Solution()
solution.duplicateZeros([1,0,2,3,0,4,5,0])
solution.duplicateZeros([1,2,3])