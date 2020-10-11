# two lists 
# Time: O(n)
# Space: O(n)
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = [x for x in A if x % 2 == 0]
        odd = [x for x in A if x % 2 == 1]
        return even + odd


solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))