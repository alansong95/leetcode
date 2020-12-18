# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return '{0:b}'.format(int(a, 2) + int(b, 2))

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = []
        
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            if carry % 2 == 1:
                result.append('1')
            else:
                result.append('0')
                
            carry //= 2
        
        if carry == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)
                