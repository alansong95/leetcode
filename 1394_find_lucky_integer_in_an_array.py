import collections

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter =  collections.Counter(arr)
        counter = map(lambda x: x if x==counter[x] else None,counter)
        ans = max(counter)
        return -1 if not ans else ans
    