class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ht = {}
        for i, row in enumerate(mat):
            ht[i] = sum(row)

        return [key for key, value in sorted(ht.items(), key=lambda x: x[1])][:k]


from Queue import PriorityQueue

class Solution2(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        q = PriorityQueue()

        for i, row in enumerate(mat):
            q.put((sum(row), i))

        res = []
        for _ in range(k):
            res.append(q.get()[1])
            
        return res