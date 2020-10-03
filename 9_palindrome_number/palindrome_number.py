# converting to str method
# class Solution(object):
#     def isPalindrome(self, x):
#         x = str(x)
#         rev = x[::-1]
#         return x == rev
        
# without converting to str
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_copy = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
        return rev == x_copy


        
solution = Solution()
print(solution.isPalindrome(1111))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
print(solution.isPalindrome(-101))
print(solution.isPalindrome(-101))