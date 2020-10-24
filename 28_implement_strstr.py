class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        return -1

solution = Solution()
print(solution.strStr('hello', 'll'))
print(solution.strStr('aaaaa', 'bba'))
print(solution.strStr('', ''))
