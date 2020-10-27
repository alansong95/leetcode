# brute force
# time:  O(2^n)
# space: O(n)
class Solution(object):
    def climbStairs(self, n):
        if n < 0:
            return 0
        elif n <= 2:
            return n
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)
        

solution = Solution()
print(solution.climbStairs(1) == 1)
print(solution.climbStairs(2) == 2)
print(solution.climbStairs(3) == 3)
print(solution.climbStairs(20) == 10946)
# print(solution.climbStairs(45) == 1836311903)