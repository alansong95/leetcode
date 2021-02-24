class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(float(a) / b),
            "*": lambda a, b: a * b
        }
        stack = []
        
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                operation = operations[token]
                stack.append(operation(num1, num2))
            else:
                stack.append(int(token))
        return stack.pop()
        