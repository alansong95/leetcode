class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 10
        output = ''
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                output += chr(int(s[i] + s[i+1]) + 96)
                i += 3
            else:
                output += chr(int(s[i]) + 96)
                i += 1
        return output
                