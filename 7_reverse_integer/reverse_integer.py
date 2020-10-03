# first solution
# time: O(n), n: number of digits
# space: O(1)
class Solution(object):
    def reverse(self, x):
        negative = False
        if x < 0:
            negative = True
            x *= -1
        y = 0
        while (x > 0):
            y = y * 10 + (x % 10)
            x = x // 10
        if self.overflow(y):
            return 0
        elif negative:
            return -y
        else:
            return y
    
    def overflow(self, x):
        if x < -(2 ** 31) or x > (2 ** 31 - 1):
            return True
        return False

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
print(solution.reverse(0))
print(solution.reverse(-2147483648))
