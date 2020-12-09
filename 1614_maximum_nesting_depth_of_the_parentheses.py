class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                max_count = max(count, max_count)
                count -= 1
        return max_count