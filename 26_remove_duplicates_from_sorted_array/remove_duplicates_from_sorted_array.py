# lazy solution
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(list(set(nums)))
        print(nums)
        return len(nums)

solution = Solution()
solution.removeDuplicates([1,1,2])
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
solution.removeDuplicates([-1,0,0,0,0,3,3])
