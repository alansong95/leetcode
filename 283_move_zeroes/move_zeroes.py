# count zeros
# Time: O(n)
# Space: O(n)
class Solution:
    def moveZeroes(self, nums):
        ans = []

        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            
        for num in nums:
            if num != 0:
                ans.append(num)
        
        for i in range(zero_count):
            ans.append(0)
        
        nums[:] = ans
        print(nums)

        

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
print(solution.moveZeroes([0,0,1]))
