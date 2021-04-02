# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


class Solution2(object):
    def isBalanced(self, root):
        return self.checkHeight(root) != -1
            
        
    def checkHeight(self, node):
        if not node:
            return 0
        
        leftHeight = self.checkHeight(node.left)
        if leftHeight == -1:
            return -1
        
        rightHeight = self.checkHeight(node.right)
        if rightHeight == -1:
            return -1
        
        heightDiff = abs(leftHeight - rightHeight)
        if heightDiff > 1:
            return -1
        
        return 1 + max(leftHeight, rightHeight)