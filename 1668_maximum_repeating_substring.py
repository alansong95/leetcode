class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        for i in range(len(sequence) // len(word), 0, -1):
            if word * i in sequence:
                return i
        return 0