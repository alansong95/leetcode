# brute force
# time:  O(2^n)
# space: O(n)
# class Solution(object):
#     def climbStairs(self, n):
#         if n < 0:
#             return 0
#         elif n <= 2:
#             return n
#         else:
#             return self.climbStairs(n-2) + self.climbStairs(n-1)

# memoization
# time: O(n)
# space: O(n)
# class Solution(object):
#     memo = {-2: 0, -1: 0, 0: 0, 1: 1, 2: 2}

#     def climbStairs(self, n):
#         if n in self.memo:
#             return self.memo[n]
#         else:
#             temp = self.climbStairs(n-2) + self.climbStairs(n-1)
#             self.memo[n] = temp
#             return temp

class Solution(object):
    def climbStairs(self, n):
        f, s = 1, 2
        for _ in range(n-1):
            f, s = s, f + s
        return f



solution = Solution()
print(solution.climbStairs(1) == 1)
print(solution.climbStairs(2) == 2)
print(solution.climbStairs(3) == 3)
print(solution.climbStairs(4) == 5)
print(solution.climbStairs(20) == 10946)
print(solution.climbStairs(45) == 1836311903)

print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(4))
print(solution.climbStairs(20))
print(solution.climbStairs(45))