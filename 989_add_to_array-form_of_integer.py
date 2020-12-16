# class Solution(object):
#     def addToArrayForm(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: List[int]
#         """
#         return [int(c) for c in str(int(''.join([str(a) for a in A])) + K)]

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        for i in range (len(A) -1, -1, -1):
            if not K: break
            K, A[i] = divmod(K + A[i], 10)
        while K:
            K, a = divmod(K, 10)
            A = [a] + A
        return A
            