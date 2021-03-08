class Solution(object):
    def generateParenthesis(self, N):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        
        backtrack('', 0, 0)
        return ans