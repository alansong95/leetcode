# sorting
# time: O(nlogn)
# space: O(1)
# class Solution(object):
#     def average(self, salary):
#         """
#         :type salary: List[int]
#         :rtype: float
#         """
#         salarySorted = sorted(salary)
#         return sum(salarySorted[1:len(salarySorted)-1]) / float((len(salarySorted)-2))
            
# linear solution
# time: O(n)
# space: O(1)
class Solution(object):
    def average(self, salary):
        return (sum(salary) - max(salary) - min(salary)) / float(len(salary) - 2)