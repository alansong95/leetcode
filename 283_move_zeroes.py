# count zeros
# Time: O(n)
# Space: O(n)
# class Solution:
#     def moveZeroes(self, nums):
#         ans = []

#         zero_count = 0
#         for num in nums:
#             if num == 0:
#                 zero_count += 1
            
#         for num in nums:
#             if num != 0:
#                 ans.append(num)
        
#         for _ in range(zero_count):
#             ans.append(0)
        
#         nums[:] = ans
#         print(nums)

# Constant space
# Time: O(n)
# Space: O(1)
class Solution:
    def moveZeroes(self, nums):
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            
        i = 0
        while i < len(nums) - zero_count:
            if nums[i] == 0:
                j = i + 1
                while nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        print(nums)        

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
print(solution.moveZeroes([0,0,1]))
