# hash table
# time: O(n)
# space: O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1
        for num in ht:
            if ht[num] > len(nums) // 2:
                return num
        
solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2,1,1,1,2,2]))
print(solution.majorityElement([]))
