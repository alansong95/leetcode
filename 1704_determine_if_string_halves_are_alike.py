class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a, b = s[0:len(s)/2], s[len(s)/2:]
        count1 = count2 = 0
        for (a1, b1) in zip(a, b):
            if a1 in vowels:
                count1 += 1
            if b1 in vowels:
                count2 += 1
        return count1 == count2
        
        