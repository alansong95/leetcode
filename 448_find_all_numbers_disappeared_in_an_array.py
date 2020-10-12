# lazy
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findDisappearedNumbers(self, nums):
        nums2 = set(range(1, len(nums)+1))
        nums = set(nums)
        return sorted(list(nums2 - nums))

        

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(solution.findDisappearedNumbers([1, 1]))