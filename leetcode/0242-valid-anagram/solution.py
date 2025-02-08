class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initial brute force solution ---
        # s_pointer, t_pointer = 0, 0
        # outer loop over s for s_pointer
        #   inner loop over t for t_pointer
        #       if s[s_pointer] == t[t_pointer], remove characters at s_pointer and t_pointer 
        # return s is empty and t is empty
        # time complexity: O(n*m) -> n is length of s, m is length of t
        # space complexity: O(n + m)

        # solution using map ---
        # loop over n, building a map of chars to counts; loop over m, decrementing from each count every time char is seen
        # time complexity: O(n + m)
        # space complexity: O(max(n, m)) -> can also be argued to be O(1) because number of characters possible is constant

        # solution using array ---
        # keep an array of counts found for each character, index is how far the character is from a in the alphabet
        # time complexity: O(n + m)
        # space complexity: O(1) because number of characters possible is constant

        # solution using sort ---
        return sorted(s) == sorted(t)
        # time complexity: O(nlogn + mlogm)
        # space complexity: O(n + m)
