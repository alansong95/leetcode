import collections
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        squares = set([i*i for i in range(int(n**0.5)+1)])
        
        queue = collections.deque([(n, 0)])
        used = set()
        
        while queue:
            t, step = queue.popleft()
            for i in squares:
                if t - i == 0:
                    return step + 1
                if t - i > 0:
                    if (t - i, step + 1) not in used:
                        queue.append((t - i, step + 1))
                        used.add((t - i, step + 1) )
        return -1