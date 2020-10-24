# time: O(n)
# space: O(1)
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         i = 0
#         while i < len(nums) and nums[i] < target:
#             i += 1
#         return i

# time: O(log(n))
# space: O(1)
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            ptr = (left + right) // 2
            if nums[ptr] == target:
                return ptr
            elif nums[ptr] > target:
                right = ptr - 1
            else:
                left = ptr + 1
        return left