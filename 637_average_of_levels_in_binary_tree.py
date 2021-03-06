# bfs
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """ 
        queue = collections.deque([(root, 0)])
        
        res = []
        while queue:
            node, level = queue.popleft()
            
            if node:
                if len(res) == level:
                    res.append([]) 
                res[level].append(node.val)
        
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        
        print res
        for i in range(len(res)):
            res[i] = float(sum(res[i])) / len(res[i])
            
        return res
        