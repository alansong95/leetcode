# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# top-down 
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.max_depth = 0
        def helper(root, depth):
            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                self.max_depth = max(self.max_depth, depth)
            
            helper(root.left, depth+1)
            helper(root.right, depth+1)
            
        helper(root, 1)
        return self.max_depth
        