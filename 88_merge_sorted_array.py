# lazy solution
# Time: O((n+m)log(n+m))
# Space: O(1)
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[len(nums1)-n:] = nums2
#         nums1[:] = sorted(nums1)

# no sorting
# Time: O(m+n)
# Space: O(m)
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         nums1_copy = nums1[:]
#         nums1[:] = []
#         p1 = 0
#         p2 = 0
#         while p1 < m and p2 < n:
#             if nums1_copy[p1] < nums2[p2]:
#                 nums1.append(nums1_copy[p1])
#                 p1 += 1
#             else:
#                 nums1.append(nums2[p2])
#                 p2 += 1
        
#         while p1 < m:
#             nums1.append(nums1_copy[p1])
#             p1 += 1
#         while p2 < n:
#             nums1.append(nums2[p2])
#             p2 += 1
        
#         print(nums1)

# no space solution
# Time: O(m+n)
# Space: O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        if p1 >= 0:
            nums1[:p+1] = nums1[:p1+1] 
        if p2 >= 0:
            nums1[:p+1] = nums2[:p2+1]
        
        print(nums1)

solution = Solution()
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
solution.merge([1], 1, [], 0)
solution.merge([0], 0, [1], 1)