
# lazy solution
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def thirdMax(self, nums):
#         if not nums:
#             return None

#         nums = sorted(list(set(nums)))
#         ind = len(nums) - 3
#         if ind < 0:
#             return nums[-1]
#         return nums[ind]

# linear time solution
# Time: O(n)
class Solution:
    def thirdMax(self, nums):
        if not nums:
            return None
            
        nums = set(nums)
        max1 = max(nums)

        if len(nums) < 3:
            return max1
        
        nums.remove(max1)
        max2 = max(nums)
        nums.remove(max2)
        return max(nums)

        ind = len(nums) - 3
        if ind < 0:
            return nums[-1]
        return nums[ind]
        
solution = Solution()
print(solution.thirdMax([3,2,1]))
print(solution.thirdMax([1,2]))
print(solution.thirdMax([2,2,3,1]))
print(solution.thirdMax([]))
print(solution.thirdMax(None))
