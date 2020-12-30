import collections
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ht = {}
        for occ in collections.Counter(arr).values():
            if occ in ht:
                return False
            ht[occ] = 1
        return True


class Solution2(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = collections.Counter(arr).values()
        return len(c) == len(set(c))
        