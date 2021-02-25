class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = 0
        word = ''
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((num, word))
                num = 0
                word = ''
            elif c == ']':
                prev_num, prev_word = stack.pop()
                word = prev_word + word * prev_num
            else:
                word += c
        return word