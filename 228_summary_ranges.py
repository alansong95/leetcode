# class Solution(object):
#     def summaryRanges(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[str]
#         """
#         if not nums:
#             return []
#         if len(nums) == 1:
#             return [str(nums[0])]
        
#         output = []
        
#         range_start = nums[0]
#         streak = nums[0]
        
#         for num in nums[1:]:
#             if num == streak + 1:
#                 streak = num
#             else:
#                 if range_start != streak:
#                     output.append(str(range_start) + '->' + str(streak))
#                     range_start = num
#                     streak = num
#                 else:
#                     output.append(str(range_start))
#                     range_start = num
#                     streak = num
                    
#         if range_start != streak:
#             output.append(str(range_start) + '->' + str(streak))
#             range_start = num
#             streak = num
#         else:
#             output.append(str(range_start))
#             range_start = num
#             streak = num
        
#         return output                

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        output = []
        i = 0
        j = 0
        while j < len(nums):
            if j+1 < len(nums) and nums[j+1] == nums[j] + 1:
                j += 1
            else:
                if (i == j):
                    output.append(str(nums[i]))
                else:
                    output.append(str(nums[i]) + '->' + str(nums[j]))
                j += 1
                i = j
        return output