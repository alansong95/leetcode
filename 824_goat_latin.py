class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        splitted = S.split(" ")
        
        for ind, word in enumerate(splitted, 1):
            if word[0].lower() not in vowel:
                word = word[1:] + word[0]
            splitted[ind] = word + 'ma' + ('a' * (ind + 1))
            
        return ' '.join(splitted)