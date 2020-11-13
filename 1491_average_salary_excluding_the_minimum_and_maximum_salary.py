# sorting
# time: O(nlogn)
# space: O(1)
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salarySorted = sorted(salary)
        return sum(salarySorted[1:len(salarySorted)-1]) / float((len(salarySorted)-2))
            