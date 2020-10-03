# converting to str method
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        rev = x[::-1]
        return x == rev
        
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
print(solution.isPalindrome(-101))