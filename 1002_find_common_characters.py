# use collections
# time: O(c); c: total num of chars
# space: O(1)
import collections
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        output = collections.Counter(A[0])
        for a in A[1:]:
            output &= collections.Counter(a)
        return output.elements()