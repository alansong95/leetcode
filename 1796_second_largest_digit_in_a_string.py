class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = ''.join([c for c in s if c.isdigit()])
        nums = sorted(set(nums))
        
        if len(nums) > 1:
            return nums[-2]
        return -1


class Solution2(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        largest = -1
        second_largest = -1
        for c in s:
            if c.isdigit():
                c = int(c)
                if c > largest:
                    second_largest = largest
                    largest = c
                elif c > second_largest and c != largest:
                    second_largest = c
        return second_largest if largest != second_largest else -1
                    
        
                    
        