class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        _dir = 0
        
        ind = 0
        while _dir == 0 and ind < len(A) - 1:
            if A[ind] < A[ind+1]:
                _dir = 1
            elif A[ind] > A[ind+1]:
                _dir = -1
            ind += 1
            
        if _dir == 0:
            return True
            
        for i in range(ind, len(A) - 1):
            if A[i+1] - A[i] != 0 and (A[i+1] - A[i]) * _dir < 0:
                return False
        return True