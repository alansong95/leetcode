import collections
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        
        queue = collections.deque()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                queue.append(nums[i][j])
        
        new_nums = [[0] * c for _ in range (r)]
        for i in range(len(new_nums)):
            for j in range(len(new_nums[i])):
                new_nums[i][j] = queue.popleft()
        
        return new_nums
        