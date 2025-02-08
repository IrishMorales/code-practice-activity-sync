class Solution:
    def isValid(self, s: str) -> bool:
        # solution using stack ---

        # keep hashmap of valid bracket pairs
        mapping = {"(":")", "{":"}", "[":"]"}

        # keep a stack
        stack = []
        
        # loop over string
        for index in range(len(s)):
            # for every opening bracket encountered, append to stack
            if s[index] in mapping:
                stack.append(s[index])
            # for every closing bracket encountered, attempt to pop its complement from stack
            else:
                # if the complement is not found, return false
                if stack and mapping[stack[-1]] == s[index]:
                    stack.pop()
                else:
                    return False

        # if the loop ends without returning false, return true if the stack is empty; false if the stack is not
        return not stack

        # time complexity: O(n)
        # space complexity: O(n)
