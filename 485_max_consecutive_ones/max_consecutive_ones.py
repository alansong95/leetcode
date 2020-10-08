# Time: O(n)
# Space: O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
        return [max_count, count][count > max_count]

solution = Solution()
print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(solution.findMaxConsecutiveOnes([0]))
print(solution.findMaxConsecutiveOnes([1]))
print(solution.findMaxConsecutiveOnes([]))