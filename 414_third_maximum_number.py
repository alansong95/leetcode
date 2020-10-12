
# lazy solution
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def thirdMax(self, nums):
        if not nums:
            return None
            
        nums = sorted(list(set(nums)))
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
