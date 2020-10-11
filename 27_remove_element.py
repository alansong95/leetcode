# remove method
# Time: O(n)
# Space: O(1)
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         try:
#             while True:
#                 nums.remove(val)
#         except:
#             print(nums)

# List comprehension 
# Time: O(n)
# Space: O(1)
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         nums[:] = [n for n in nums if n != val]
#         print(nums)

# Lambda filter
# Time: O(n)
# Space: O(1)
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         nums[:] = list(filter(lambda x: x != val, nums))
#         print(nums)

# naive way
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums:val: int
        :rty List[int]
        :type pe: int
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p

solution = Solution()
solution.removeElement([3,2,2,3], 3)
