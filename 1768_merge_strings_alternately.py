class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return ''.join([w1+w2 for w1, w2 in zip_longest(word1, word2, fillvalue='')])