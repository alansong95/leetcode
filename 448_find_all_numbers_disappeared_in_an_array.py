# lazy
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         nums2 = set(range(1, len(nums)+1))
#         nums = set(nums)
#         return sorted(list(nums2 - nums))

        
# linear time solution
# Time: O(n)
# Space: O(n)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        ht = {}
        for num in nums:
            ht[num] = num
        
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in ht:
                ans.append(i)
        return ans
        
        

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(solution.findDisappearedNumbers([1, 1]))