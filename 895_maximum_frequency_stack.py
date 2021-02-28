# O(log n) heap
import collections
import heapq

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


# O(1)
class FreqStack2(object):
    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.freq[x] += 1
        if self.freq[x] > self.maxfreq:
            self.maxfreq = self.freq[x]
        self.group[self.freq[x]].append(x)
        
        
    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        
        return x

