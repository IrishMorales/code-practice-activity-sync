class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initial solution (sliding window and set) ---
        substr_chars = set()
        start = 0
        max_length = 0

        for index, char in enumerate(s):
            if char in substr_chars:
                while char in substr_chars:
                    substr_chars.remove(s[start])
                    start += 1
            else:
                max_length = max(max_length, index - start + 1)
            substr_chars.add(char)
        return max_length

        # edge case: s.length == 0
        
        # time complexity: O(n)
        # space complexity: O(1)
