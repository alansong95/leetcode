class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.findall('\w+', paragraph.lower())
        return collections.Counter([word for word in words if word not in banned]).most_common(1)[0][0]