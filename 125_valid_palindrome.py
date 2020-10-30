# string manipulation
# time: O(n)
# space: 1
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = (''.join(x for x in s if x.isalnum())).lower()
        return s == s[::-1]

solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))
print(solution.isPalindrome('race a car'))