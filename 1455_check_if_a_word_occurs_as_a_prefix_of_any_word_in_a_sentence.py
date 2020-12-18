class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        splitted = sentence.split(' ')
        for ind, word in enumerate(splitted):
            if word.startswith(searchWord):
                return ind + 1
        return -1
            