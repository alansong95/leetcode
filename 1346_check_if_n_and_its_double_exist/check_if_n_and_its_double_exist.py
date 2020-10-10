# brute force
# Time: O(n^2)
# Space: O(1)

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if not arr or len(arr) == 0:
            return False
            
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j] * 2 or arr[i] * 2 == arr[j]:
                    return True
        return False

solution = Solution()
print(solution.checkIfExist([10,2,5,3]))
print(solution.checkIfExist([7,1,14,11]))
print(solution.checkIfExist([3,1,7,11]))
print(solution.checkIfExist(None))
print(solution.checkIfExist([]))