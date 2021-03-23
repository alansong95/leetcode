class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number = [d for d in number if d.isdigit()]
        q, r = divmod(len(number), 3)
        number = [d+'-' if i % 3 == 2 else d for i, d in enumerate(number)]
        if r == 0:
            number[-1] = number[-1][:1]
        if r == 1:
            number[-2], number[-3] = number[-2][:1], number[-3] + '-'
        return ''.join(number)
        