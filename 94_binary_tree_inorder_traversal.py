# recursion
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if root == None:
                return
            helper(root.left)
            self.output.append(root.val)
            helper(root.right)

        self.output = []
        helper(root)
        return self.output


# cleaner recursion
class Solution2(object):
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)


# one line recursion
class Solution3(object):
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# iterative
class Solution4(object):
    def inorderTraversal(self, root):
        stack = [(root, False)]
        res = []
        
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))
        return res