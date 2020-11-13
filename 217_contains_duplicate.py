# import statistics
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         return len(statistics.multimode(nums)) != len(nums)

# implement using sorting
# time: O(nlogn)
# space: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortedNums = sorted(nums)
        for i in range(1, len(sortedNums)):
            if sortedNums[i-1] == sortedNums[i]:
                return True
        return False