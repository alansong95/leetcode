class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return [int(c) for c in str(int(''.join([str(a) for a in A])) + K)]