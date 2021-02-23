class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chars = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        
        def helper(digits, acc):
            if not digits:
                if acc:
                    res.append(acc)
                return 
            
            for c in chars[int(digits[0])-2]:
                helper(digits[1:], acc + c)
        
        helper(digits, '')
        return res