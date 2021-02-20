class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remove = set([])
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop(-1)
                else:
                    remove.add(i)
        
        for i in stack:
            remove.add(i)
           
        new_string = ''
        for i, c in enumerate(s):
            if i not in remove:
                new_string += c
        
        return new_string