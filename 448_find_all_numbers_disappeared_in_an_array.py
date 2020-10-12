# lazy
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         nums2 = set(range(1, len(nums)+1))
#         nums = set(nums)
#         return sorted(list(nums2 - nums))

        
# linear time solution
# Time: O(n)
# Space: O(n)
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         ht = {}
#         for num in nums:
#             ht[num] = num
        
#         ans = []
#         for i in range(1, len(nums) + 1):
#             if i not in ht:
#                 ans.append(i)
#         return ans
        
        
# linear time const space solution
# Time: O(n)
# Space: O(1)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans = []

        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(solution.findDisappearedNumbers([1, 1]))