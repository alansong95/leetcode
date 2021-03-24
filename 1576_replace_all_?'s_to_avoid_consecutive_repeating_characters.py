class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = list(s)
        for i in range(len(ls)):
            if ls[i] == '?':
                for c in 'abc':
                    if (i == 0 or ls[i-1] != c) and (i+1 == len(s) or ls[i+1] != c):
                        ls[i] = c
                        break

        return ''.join(ls)