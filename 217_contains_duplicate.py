import statistics
class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(statistics.multimode(nums)) != len(nums)