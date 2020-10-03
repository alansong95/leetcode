# first solution
# time: O(n), n: number of digits
# space: O(1)
# class Solution(object):
#     def reverse(self, x):
#         negative = x < 0
#         x = abs(x)
#         y = 0
#         while (x > 0):
#             y = y * 10 + (x % 10)
#             x = x // 10
#         if self.overflow(y):
#             return 0
#         return -y if negative else y 
    
#     def overflow(self, x):
#         if x < -(2 ** 31) or x > (2 ** 31 - 1):
#             return True
#         return False

# string conversion
# time: O(n)
# space: O(1)
class Solution(object):
    def reverse(self, x):
        sign = [1, -1][x < 0]
        reverse = sign * int(str(abs(x))[::-1])
        return 0 if reverse < -(2 ** 31) or reverse > (2 ** 31 - 1) else reverse

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
print(solution.reverse(0))
print(solution.reverse(-2147483648))
