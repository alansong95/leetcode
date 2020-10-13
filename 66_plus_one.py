# lazy solution
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         return [int(x) for x in str(int(''.join([str(x) for x in digits]))+1)]

# 
class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + carry
            if digits[i] >= 10:
                carry = 1
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
            else:
                break
        return digits

solution = Solution()
test_cases = [[1,2,3], [4,3,2,1], [0], [9], [9, 9]]
for tc in test_cases:
    print(solution.plusOne(tc))