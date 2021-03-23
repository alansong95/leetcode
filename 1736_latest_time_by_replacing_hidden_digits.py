class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        ls = [int(c) if c.isdigit() else c for c in time]
        for i, c in enumerate(ls):
            if c == '?':
                if i == 0:
                    if type(ls[1]) == int and ls[1] > 3:
                        ls[0] = 1
                    else:
                        ls[0] = 2
                elif i == 1:
                    if ls[0] == 2:
                        ls[1] = 3
                    else:
                        ls[1] = 9
                elif i == 3:
                    ls[3] = 5
                elif i == 4:
                    ls[4] = 9
        return ''.join([str(c) for c in ls])

        
        
        