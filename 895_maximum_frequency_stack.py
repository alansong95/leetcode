# O(log n) heap
import collections
class FreqStack(object):
    def __init__(self):
        self.heap = []
        self.m = collections.defaultdict(int)
        self.index = 0
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.m[x] += 1
        heapq.heappush(self.heap, (-self.m[x], -self.index, x))
        self.index += 1
        
    def pop(self):
        """
        :rtype: int
        """
        removed = heapq.heappop(self.heap)
        self.m[removed[2]] -= 1
        return removed[2]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()