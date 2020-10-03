# first solution
# class Solution(object):
#     dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     def romanToInt(self, s):
#         sum = 0
#         prev = ''
#         for i, c in enumerate(s):
#             if prev == 'I' and (c == 'V' or c == 'X'): 
#                 sum -= 2
#             elif prev == 'X' and (c == 'L' or c == 'C'):
#                 sum -= 20
#             elif prev == 'C' and (c == 'D' or c == 'M'):
#                 sum -= 200
#             sum = sum + self.dict[c]
#             prev = c
#         return sum

# more general solution
# class Solution(object):
#     _map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     def romanToInt(self, s):
#         _sum = 0
#         prev = 0
#         for c in s[::-1]:
#             if self._map[c] >= prev:
#                 _sum += self._map[c]
#             else:
#                 _sum -= self._map[c]
#             prev = self._map[c]
#         return _sum

# a solution that does not need reverse
class Solution(object):
    def romanToInt(self, s):
        _map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        _sum = 0
        for i in range(len(s) - 1):
            if _map[s[i]] < _map[s[i+1]]:
                _sum -= _map[s[i]] 
            else:
                _sum += _map[s[i]]
        return _sum + _map[s[-1]]


solution = Solution()
print(solution.romanToInt('III'))
print(solution.romanToInt('IV'))
print(solution.romanToInt('IX'))
print(solution.romanToInt('LVIII'))
print(solution.romanToInt('MCMXCIV'))
        