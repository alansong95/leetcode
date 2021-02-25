# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if node:
                if len(res) > level:
                    res[level].append(node.val)
                else:
                    res.append([node.val])
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res