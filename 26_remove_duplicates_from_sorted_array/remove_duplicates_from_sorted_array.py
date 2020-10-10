# lazy solution
# class Solution(object):
#     def removeDuplicates(self, nums):
#         nums[:] = sorted(list(set(nums)))
#         print(nums)
#         return len(nums)

# not lazy 
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        p = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                continue
            nums[p] = nums[i]
            p += 1
        print(nums, ' ', p)
        return p

solution = Solution()
solution.removeDuplicates([1,1,2])
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
solution.removeDuplicates([-1,0,0,0,0,3,3])
