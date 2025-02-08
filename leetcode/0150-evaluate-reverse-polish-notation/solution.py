class Solution:
    def evalOperation(self, operand1: int, operand2: int, operator: str) -> int:
        if operator == '+':
            return operand2 + operand1
        elif operator == '-':
            return operand2 - operand1
        elif operator == '*':
            return operand2 * operand1
        else:
            return int(operand2 / operand1) # truncate towards 0

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for index in range(len(tokens)):
            if tokens[index] not in '+-*/':
                stack.append(int(tokens[index]))
            else:
                new_val = self.evalOperation(stack.pop(), stack.pop(), tokens[index])
                stack.append(new_val)
        return stack.pop()

        # edge case: if only one token, it will always be an integer to return

        # time complexity: O(n)
        # space complexity: O(n) or roughly O(n/2) in practice
