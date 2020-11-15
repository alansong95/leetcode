# import collections
# class Solution(object):
#     def countCharacters(self, words, chars):
#         """
#         :type words: List[str]
#         :type chars: str
#         :rtype: int
#         """
#         output = 0
#         charsCounter = collections.Counter(chars)
#         for word in words:
#             wordCounter = collections.Counter(word)
#             if (charsCounter & wordCounter) == wordCounter:
#                 output += len(word)
#         return output

# using hash table
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        output = 0
        ht = {}
        
        for c in chars:
            ht[c] = ht.get(c, 0) + 1
        
        addFlag = 1
        for word in words:
            addFlag = 1
            tempHt = ht.copy()
            for c in word:
                if c in tempHt and tempHt[c] > 0:
                    tempHt[c] -= 1
                else:
                    addFlag = 0
                    break
            if addFlag == 1:
                output += len(word)
            
        return output
            