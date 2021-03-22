import collections

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        ht = collections.defaultdict(int)
        
        res = -1
        for i in range(lowLimit, highLimit+1):
            ht[self.h(i)] += 1
            if ht[self.h(i)] > res:
                res = ht[self.h(i)]
        
        return res
            
    def h(self, num):
        _sum = 0
        
        num_str = str(num)
        for c in num_str:
            _sum += int(c)
        return _sum

class Solution2(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        ht = collections.defaultdict(int)
        
        res = -1
        for i in range(lowLimit, highLimit+1):
            hashed_value = self.h(i)
            ht[hashed_value] += 1
            if ht[hashed_value] > res:
                res = ht[hashed_value]
        return res
            
    def h(self, num):
        return sum([int(c) for c in str(num)])