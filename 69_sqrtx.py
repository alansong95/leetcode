# time: O(n)
# space: O(1)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        elif x == 2:
            return 1
        
        for i in range(1, x):
            if i * i > x:
                return i-1
            elif i * i == x:
                return i
            i += 1
        

solution = Solution()
print(solution.mySqrt(0) == 0)
print(solution.mySqrt(1) == 1)
print(solution.mySqrt(2) == 1)
print(solution.mySqrt(3) == 1)
print(solution.mySqrt(4) == 2)
print(solution.mySqrt(5) == 2)
print(solution.mySqrt(6) == 2)
print(solution.mySqrt(7) == 2)
print(solution.mySqrt(8) == 2)
print(solution.mySqrt(9) == 3)
print(solution.mySqrt(10) == 3)
print(solution.mySqrt(1245) == 35)