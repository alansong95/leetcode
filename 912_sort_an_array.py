# merge sort
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        
        middle = int(len(nums) / 2)
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        lp = rp = 0
        res = []
        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                res.append(left[lp])
                lp += 1
            else:
                res.append(right[rp])
                rp += 1
        
        res.extend(left[lp:])
        res.extend(right[rp:])
        return res