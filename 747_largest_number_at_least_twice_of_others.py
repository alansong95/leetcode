# copy and sort 
# time: O(nlogn)
# space: O(n)
# class Solution(object):
#     def dominantIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return 0
#         nums_sorted = sorted(nums)
#         if nums_sorted[-1] >= nums_sorted[-2] * 2:
#             return nums.index(nums_sorted[-1])
#         else:
#             return -1
        
# linear scan
# time: O(n)
# space: O(1)
class Solution(object):
    def dominantIndex(self, nums):
        max_index = nums.index(max(nums))
        for i in range(len(nums)):
            if i != max_index and nums[i] * 2 > nums[max_index]:
                return -1
        return max_index
        

solution = Solution()
# print(solution.dominantIndex([]))
print(solution.dominantIndex([0]))
print(solution.dominantIndex([0, 0]))
print(solution.dominantIndex([3, 6, 1, 0]))
print(solution.dominantIndex([1, 2, 3, 4]))
print(solution.dominantIndex([0, 0, 0, 1]))