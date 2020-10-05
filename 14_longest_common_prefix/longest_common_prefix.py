# brute force
# Time: O(nm), n: length of array, m: avg. length of strings
# Space: O(1)
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         longest = strs[0] if strs else ''

#         for _str in strs[1:]:
#             i = 0
#             while i < len(longest) and i < len(_str) and longest[i] == _str[i]:
#                 i += 1
#             longest = longest[:i]
#         return longest
        
# vertical scanning
# Time: O(n), n: sum of lengths of strs
# Space: O(1)
class Solution(object):
    def longestCommonPrefix(self, strs):
        longest = ''
        j = 0
        going = True if strs and strs[0] else False
        while going and j < len(strs[0]):
            common = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != common:
                    going = False
                    break
            if going:
                longest += common
                j += 1
        return longest


solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix([]))
print(solution.longestCommonPrefix([""]))
print(solution.longestCommonPrefix(["a"]))
print(solution.longestCommonPrefix(["ab", "a"]))