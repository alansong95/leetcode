class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = s[0]
        power = 1
        max_power = 1
        
        for c in s[1:]:
            if c == curr:
                power += 1
            else:
                if power > max_power:
                    max_power = power
                curr = c
                power = 1
                    
        return max(max_power, power)
        