# hash table
# time: O(J + S)
# space: O(J)
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ht = {}
        count = 0
        for j in J:
            if j not in ht:
                ht[j] = 1
        
        for s in S:
            if s in ht:
                count += 1
        return count