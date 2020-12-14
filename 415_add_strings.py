# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         return str(int(num1) + int(num2))

# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         res = ''
#         prev_carry = 0
#         carry = 0

#         num1 = num1[::-1]
#         num2 = num2[::-1]
#         while len(num1) < len(num2): num1 += '0'
#         while len(num2) < len(num1): num2 += '0'
            
        
#         for n1, n2 in zip(num1, num2):
#             _sum = (ord(n1) - ord('0')) + (ord(n2) - ord('0'))
#             carry = (prev_carry + _sum) // 10
#             _sum = (prev_carry + _sum) % 10
#             res += str(_sum)
#             prev_carry = carry
#         if carry == 1:
#             res += '1'
#         return res[::-1]

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        carry = 0

        n = max(len(num1), len(num2))
        num1, num2 = num1.zfill(n), num2.zfill(n)
            
        for _, (n1, n2) in enumerate(zip(num1[::-1], num2[::-1])):
            _sum = (ord(n1) - ord('0')) + (ord(n2) - ord('0')) + carry
            carry = _sum // 10
            _sum = _sum % 10
            res.append(str(_sum))
            
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)