class Solution(object):
    keyboard_rows = [
            ['Q','W','E','R','T','Y','U','I','O','P'],
            ['A','S','D','F','G','H','J','K','L'],
            ['Z','X','C','V','B','N','M']
        ]
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        
        for word in words:
            row = self.getRow(word[0])
            if self.sameRow(word, row):
                output.append(word)
        return output
            
            
    def getRow(self, char):
        for ind, row in enumerate(self.keyboard_rows):
            if char.upper() in row:
                return ind
    
    def sameRow(self, word, row):
        for c in word[1:]:
            if c.upper() not in self.keyboard_rows[row]:
                return False
        return True
                    