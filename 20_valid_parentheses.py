# brute force
# Time: O(s): length of string
# Space: O(1)
# class Solution(object):
#     def isValid(self, s):
#         if len(s) <= 1:
#             return False
#         _dict = {'(': -1, '{': -1, '[': -1, ')': 1, '}': 1, ']': 1}
#         _stack = []
#         for c in s:
#             if _dict[c] == -1:
#                 _stack.append(c)
#             else:
#                 if len(_stack) > 0:
#                     opener = _stack.pop()
#                     if ord(opener)+1 == ord(c) or ord(opener)+2 == ord(c):
#                         continue
#                     else:
#                         return False
#                 else:
#                     return False

#         if len(_stack) > 0:
#             return False
#         return True

# better solution
class Solution(object):
    def isValid(self, s):
        _dict = {'(': ')', '{': '}', '[': ']'}
        _stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                _stack.append(c)
            else:
                if len(_stack) > 0:
                    if _dict[_stack.pop()] == c:
                        continue
                return False
        return True if len(_stack) == 0 else False


class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if len(stack) == 0 or dic[stack.pop(-1)] != c:
                    return False
        return len(stack) == 0


solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))
print(solution.isValid("{[]}"))
print(solution.isValid("{{"))
print(solution.isValid("){"))