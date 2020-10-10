# remove method
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            while True:
                nums.remove(val)
        except:
            print(nums)

solution = Solution()
solution.removeElement([3,2,2,3], 3)
