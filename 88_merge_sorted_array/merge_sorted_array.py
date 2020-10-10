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
        true_m = len(nums1) - 1
        for i in range(len(nums2)):
            nums1[true_m] = nums2[i]
            true_m -= 1
        nums1 = sorted(nums1)
        print(nums1)

solution = Solution()
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)