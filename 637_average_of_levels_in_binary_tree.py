import collections
# bfs
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
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
        
        for i in range(len(res)):
            res[i] = float(sum(res[i])) / len(res[i])
            
        return res
        
# dfs recursion
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """ 
        lvlcnt = collections.defaultdict(int)
        lvlsum = collections.defaultdict(int)

        def dfs(node, level):
            if not node:
                return
            lvlcnt[level] += 1
            lvlsum[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        dfs(root, 0)
        return [float(lvlsum[i]) / lvlcnt[i] for i in range(len(lvlcnt))]


# dfs with stack
class Solution3(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """ 
        lvlcnt = collections.defaultdict(int)
        lvlsum = collections.defaultdict(int)

        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                lvlcnt[level] += 1
                lvlsum[level] += node.val
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))

        return [float(lvlsum[i]) / lvlcnt[i] for i in range(len(lvlcnt))]