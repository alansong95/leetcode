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
    
class Solution2(object):
    def postorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
        
    
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            self.helper(root.right, res)
            res.append(root.val)