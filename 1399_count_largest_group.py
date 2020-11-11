# hash table & two passes
# time: O(n)
# space: O(n)
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        ht = {}
        for num in range(1, n+1):
            sum_of_digit = 0
            for d in str(num):
                sum_of_digit += int(d)
            if sum_of_digit in ht:
                ht[sum_of_digit].append(num)
            else:
                ht[sum_of_digit] = [num]
        
        largest_size = 0
        count = 0
        for key in ht:
            if len(ht[key]) > largest_size:
                largest_size = len(ht[key])
                count = 1
            elif len(ht[key]) == largest_size:
                count += 1
        return count