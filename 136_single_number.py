# hash table
# time: O(n)
# space: O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                del table[num]
        return table.keys()[0]