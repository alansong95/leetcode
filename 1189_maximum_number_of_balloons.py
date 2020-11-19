class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = collections.Counter(text)
        counter['l'] = counter['l'] / 2
        counter['o'] = counter['o'] / 2
        
        output = counter.get('b', 0)
        
        for c in 'alon':
            temp = counter.get(c, 0)
            if temp < output:
                output = temp
        return output