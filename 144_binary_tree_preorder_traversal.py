# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def preorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         output = []
#         return self.helper(root, output)
    
#     def helper(self, root, output):
#         if root == None:
#             return output
#         output.append(root.val)
#         output = self.helper(root.left, output)
#         output = self.helper(root.right, output)
#         return output

class Solution(object):
    def preorderTraversal(self, root):
        def helper(root):
            if root == None:
                return
            self.output.append(root.val)
            helper(root.left)
            helper(root.right)
        self.output = []
        helper(root)
        return self.output
        