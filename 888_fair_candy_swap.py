# class Solution(object):
#     def fairCandySwap(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: List[int]
#         """
#         sumA = sum(A)
#         sumB = sum(B)
#         diff = (sumA - sumB) / 2
        
#         ht = {}
#         for a in A:
#             ht[a] = a
        
#         for b in B:
#             if (b + diff) in ht:
#                 return [ht[b+diff], b]

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        diff = (sumA - sumB) / 2
        
        _set = set()
        for a in A:
            _set.add(a)
        
        for b in B:
            if (b + diff) in _set:
                return [b+diff, b]