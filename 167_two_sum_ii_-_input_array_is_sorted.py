# brute force
# time: O(n)
# space: O(1)
# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(numbers)):
#             for j in range(i+1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1, j+1]
#                 if numbers[i] + numbers[j] > target:
#                     break

# hash table
# time: O(n)
# space: O(n)
# class Solution(object):
#     def twoSum(self, numbers, target):
#         table = {}
        
#         for i, num in enumerate(numbers):
#             if (target - num) in table:
#                 return [table[target-num]+1, i+1]
#             if num not in table:
#                 table[num] = i

# two pointers
# time: O(n)
# space: O(1)
class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l <= r:
            _sum = numbers[l] + numbers[r]
            if _sum == target:
                return [l+1, r+1]
            elif _sum > target:
                r -= 1
            else:
                l += 1
