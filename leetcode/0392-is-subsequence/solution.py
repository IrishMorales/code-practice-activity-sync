class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # initial solution ---
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        sPointer = 0
        for letter in t:
            if s[sPointer] == letter:
                sPointer += 1
            if sPointer == len(s):
                return True
        return False
        # time complexity: O(n)
        # space complexity: O(1)

