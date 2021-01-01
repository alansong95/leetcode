class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        arr = ' '.join(words)
        return [word for word in words if arr.count(word) >= 2]