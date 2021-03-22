class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        keyIndex = {'type': 0, 'color': 1, 'name': 2}
        res = 0
        
        for item in items:
            if item[keyIndex[ruleKey]] == ruleValue:
                res += 1
        return res


class Solution2(object):
    keyIndex = {'type': 0, 'color': 1, 'name': 2}
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        return sum(1 for item in items if item[self.keyIndex[ruleKey]] == ruleValue)