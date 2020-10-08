# Time: O(n)
# Space: O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        return max(count, max_count)

solution = Solution()
print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(solution.findMaxConsecutiveOnes([0]))
print(solution.findMaxConsecutiveOnes([1]))
print(solution.findMaxConsecutiveOnes([]))