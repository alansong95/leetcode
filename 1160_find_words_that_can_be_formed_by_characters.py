class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        output = 0
        charsCounter = collections.Counter(chars)
        for word in words:
            wordCounter = collections.Counter(word)
            if (charsCounter & wordCounter) == wordCounter:
                output += len(word)
        return output
            