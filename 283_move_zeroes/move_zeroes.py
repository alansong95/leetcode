# brute force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)-1):
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        print(nums)

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))