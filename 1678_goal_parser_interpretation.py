# class Solution(object):
#     def interpret(self, command):
#         """
#         :type command: str
#         :rtype: str
#         """
#         output = ""
#         stack = []
#         for c in command:
#             if c == 'G':
#                 output += 'G'
#             elif c == '(':
#                 stack.append(c)
#             elif c == ')':
#                 new_c = ''.join(stack) + ')'
#                 if new_c == '()':
#                     output += 'o'
#                 elif new_c == '(al)':
#                     output += 'al'
#                 stack = []
#             else:
#                 stack.append(c)
#         return output

class Solution(object):
    def interpret(self, command):
        return command.replace('()', 'o').replace('(al)', 'al')