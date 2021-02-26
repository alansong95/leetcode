# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# recursive
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# iterative
class Solution2(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        stack = [(root, targetSum)]
        
        while stack:
            node, target = stack.pop()
            if node:
                target = target - node.val
                if node.left is None and node.right is None and target == 0:
                    return True

                stack.append((node.left, target))
                stack.append((node.right, target))
        return False