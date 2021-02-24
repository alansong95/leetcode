class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(T)
        
        for i, t in enumerate(T):
            while stack and stack[-1][1] < t:
                ind, temp = stack.pop()
                ans[ind] = i - ind
            stack.append((i, t))
        return ans