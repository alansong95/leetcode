# lazy solution
# class Solution(object):
#     def removeDuplicates(self, nums):
#         nums[:] = sorted(list(set(nums)))
#         print(nums)
#         return len(nums)

# not lazy 
# Time: O(n)
# Space: O(1)
# class Solution(object):
#     def removeDuplicates(self, nums):
#         p = 0
#         for i in range(len(nums)):
#             if i + 1 < len(nums) and nums[i] == nums[i+1]:
#                 continue
#             nums[p] = nums[i]
#             p += 1
#         print(nums, ' ', p)
#         return p

# two passes
# Time: O(n)
# Space: O(1)
# class Solution(object):
#     def removeDuplicates(self, nums):
#         # pass 1: count unique elements
#         unique = 0
#         prev = None
#         for num in nums:
#             if prev != num:
#                 unique += 1
#             prev = num
        
#         # pass 2: rearrange 
#         p = 0
#         prev = None
#         for i in range(len(nums)):
#             if prev != nums[i]:
#                 nums[p] = nums[i]
#                 p += 1
#             prev = nums[i]
#             i += 1
#         return unique

# two pointers
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        wp = 1
        for rp in range(1, len(nums)):
            if nums[rp] != nums[rp - 1]:
                nums[wp] = nums[rp]
                wp += 1
            rp += 1
        print(nums[:wp])
        return wp
    
solution = Solution()
solution.removeDuplicates([1,1,2])
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
solution.removeDuplicates([-1,0,0,0,0,3,3])
