class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0] * n
        arr = [[0, 0, 0, 0, 1] for e in arr]
        print arr
        for i in range(n):
            for j in range(4-1, -1, -1):
                if i == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = sum(arr[i-1][j:])
        return sum(arr[-1])
            
            