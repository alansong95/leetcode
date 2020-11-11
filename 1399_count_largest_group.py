# hash table & two passes
# time: O(n)
# space: O(n)
# class Solution(object):
#     def countLargestGroup(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ht = {}
#         for num in range(1, n+1):
#             sum_of_digit = 0
#             for d in str(num):
#                 sum_of_digit += int(d)
#             if sum_of_digit in ht:
#                 ht[sum_of_digit].append(num)
#             else:
#                 ht[sum_of_digit] = [num]

#         largest_size = 0
#         count = 0
#         for key in ht:
#             if len(ht[key]) > largest_size:
#                 largest_size = len(ht[key])
#                 count = 1
#             elif len(ht[key]) == largest_size:
#                 count += 1
#         return count

# one pass
# class Solution(object):
#     def countLargestGroup(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ht = {}
#         largest_size = 0
#         count = 0
#         for num in range(1, n+1):
#             sod = self.sum_of_digits(num)
#             if sod in ht:
#                 ht[sod].append(num)
#             else:
#                 ht[sod] = [num]
#             if len(ht[sod]) > largest_size:
#                 largest_size = len(ht[sod])
#                 count = 1
#             elif len(ht[sod]) == largest_size:
#                 count += 1
#         return count
    
#     def sum_of_digits(self, num):
#         sod = 0
#         while num > 0:
#             sod = sod + (num % 10)
#             num = num // 10
#         return sod

# clean up code with dictionary.get
# class Solution(object):
#     def countLargestGroup(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ht = {}
#         largest_size = 0
#         count = 0
#         for num in range(1, n+1):
#             sod = self.sum_of_digits(num)
#             ht[sod] = ht.get(sod, 0) + 1
            
#             if ht[sod] > largest_size:
#                 largest_size = ht[sod]
#                 count = 1
#             elif ht[sod] == largest_size:
#                 count += 1
#         return count
    
#     def sum_of_digits(self, num):
#         sod = 0
#         while num > 0:
#             sod = sod + (num % 10)
#             num = num // 10
#         return sod

# one line solution
import statistics
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(statistics.multimode(sum(map(int, str(i))) for i in range(1, n+1)))