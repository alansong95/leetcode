# lazy solution if not in place
# Time: O(nlogn)
# Space: O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[len(nums1)-n:] = nums2
        nums1 = sorted(nums1)

solution = Solution()
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)