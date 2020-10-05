# brute force
# Time: O(nm), n: length of array, m: avg. length of strings
# Space: O(1)
class Solution(object):
    def longestCommonPrefix(self, strs):
        longest = strs[0]

        for _str in strs[1:]:
            i = 0
            while i < len(longest) and i < len(_str) and longest[i] == _str[i]:
                i += 1
            longest = longest[:i]
        return longest
        

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))