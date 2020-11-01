# brute force
# time: O(n)
# space: O(1)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i, j]
                if numbers[i] + numbers[j] > target:
                    break
                

solution = Solution()
print(solution.