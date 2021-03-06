# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """
#         first = nums[0:n]
#         second = nums[n:]
#         output = []
#         for i in range(n):
#             output.append(first[i])
#             output.append(second[i])
#         return output

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n+i])
        return output