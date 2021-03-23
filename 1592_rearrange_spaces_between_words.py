class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        num_spaces = text.count(' ')
        splited = text.split(' ')
        splited = [c for c in splited if c != '']
        if len(splited) == 1:
            return ''.join(splited) + ' ' * num_spaces 
        
        q, r = divmod(num_spaces, len(splited) - 1)
        res = [c + ' ' * q for c in splited[:-1]]
        res.append(splited[-1] + ' ' * r)
        return ''.join(res)