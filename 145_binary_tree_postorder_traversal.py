# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if root == None:
                return
            helper(root.left)
            helper(root.right)
            self.output.append(root.val)
        self.output = []
        helper(root)
        return self.output