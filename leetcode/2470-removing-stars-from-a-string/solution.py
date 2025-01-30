class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # initial solution ---
        # remainingOperations = 0
        # loop from end of s to start {
        #     if (s[index] == "*") ++remainingOperations, remove s[index]
        #     else if (remainingOperations) --remainingOperations, remove s[index]
        # }
        # time complexity: O(n^2)
        # space complexity: O(1)

        # optimal solution: use stack ---
        stack = []
        for index in range(len(s)):
            if (s[index] == '*'):
                stack.pop()
            else:
                stack.append(s[index])
        return ''.join(stack)
        # time complexity: O(n)
        # space complexity: O(n)
