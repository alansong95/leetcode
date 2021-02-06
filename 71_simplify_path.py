class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        
        for e in path.split("/"):
            if e == '..':
                if stack:
                    stack.pop()
            elif not e or e == '.':
                continue
            else:
                stack.append(e)
        
        return '/' + '/'.join(stack)
            