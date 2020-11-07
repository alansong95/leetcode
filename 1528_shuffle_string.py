class Solution(object):
    def restoreString(self, s, indices):
        output = [None] * len(s)
        for i, ind in enumerate(indices):
            output[ind] = s[i]
        return ''.join(output)
        