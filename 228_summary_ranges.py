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
        
        range_start = nums[0]
        streak = nums[0]
        
        for num in nums[1:]:
            if num == streak + 1:
                streak = num
            else:
                if range_start != streak:
                    output.append(str(range_start) + '->' + str(streak))
                    range_start = num
                    streak = num
                else:
                    output.append(str(range_start))
                    range_start = num
                    streak = num
                    
        if range_start != streak:
            output.append(str(range_start) + '->' + str(streak))
            range_start = num
            streak = num
        else:
            output.append(str(range_start))
            range_start = num
            streak = num
        
        return output                