# two potiners
# Time: O(n)
# Space: O(1)
class Solution:
    def pivotIndex(self, nums):
        _sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == _sum - left_sum - num:
                return i
            else:
                left_sum += num
        return -1


solution = Solution()

print(solution.pivotIndex([1,7,3,6,5,6]) == 3)
print(solution.pivotIndex([1,2,3,4]) == -1)
print(solution.pivotIndex([1]) == 0)
print(solution.pivotIndex([-1,-1,-1,-1,-1,0]) == 2)

print(solution.pivotIndex([1,7,3,6,5,6]))
print(solution.pivotIndex([1,2,3,4]))
print(solution.pivotIndex([1]))
print(solution.pivotIndex([-1,-1,-1,-1,-1,0]))