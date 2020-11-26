import collections
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counterA = collections.Counter(A.split(' '))
        counterB = collections.Counter(B.split(' '))
        output = (counterA - counterB) | (counterB - counterA)
        
        for word, count in counterA.items():
            if count > 1:
                del output[word]
        
        for word, count in counterB.items():
            if count > 1:
                del output[word]
                
        return output