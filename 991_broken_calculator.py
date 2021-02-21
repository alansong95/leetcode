class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        _count = 0
        
        while Y > X:
            if Y % 2 == 1:
                Y += 1
            else:
                Y /= 2
            _count += 1
            
        return _count + X - Y