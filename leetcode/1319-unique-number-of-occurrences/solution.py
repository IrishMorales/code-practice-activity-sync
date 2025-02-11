from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # brute force solution ---
        # keep a slow_pointer (outer loop) and fast_pointer (inner loop)
        # count number of times arr[slow_pointer] occurs using the fast_pointer
        # store count in a set
        # return False if count already exists in set
        # if loop ends, return True
        # time complexity: O(n^2)
        # space complexity: O(n)

        # improved solution ---
        # loop over arr, build a frequency map of how often we see each number
        freq_map = Counter(arr)
        # build a set out of map values, if set length == map values length then no duplicates so we return True
        return len(set(freq_map.values())) == len(freq_map.values())
        # time complexity: O(n)
        # space complexity: O(n)
