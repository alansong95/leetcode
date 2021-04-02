# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, lo, hi):
            if hi < lo:
                return None
            
            idx = (hi + lo) // 2
            node = TreeNode(nums[idx])
            node.left = helper(nums, lo, idx-1)
            node.right = helper(nums, idx+1, hi)
            return node
            
        return helper(nums, 0, len(nums)-1)