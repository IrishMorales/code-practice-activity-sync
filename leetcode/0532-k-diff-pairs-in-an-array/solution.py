from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # brute force solution ---
        # keep a slow_pointer (outer loop) and fast_pointer (inner loop)
        # for each nums[slow_pointer] check if nums[slow_pointer] - nums[fast_pointer] == k
        # if it is, check if the pair is already existing in a dictionary of answers (both the keys and values)
        # if it isn't, add it to the dictionary; return the amount of keys in the dictionary
        # time complexity: O(n^2)
        # space complexity: O(n)

        # improved solution ---
        # observation: there will only be at most one complement for each number where nums[index] - complement == k
        
        freq_map = Counter(nums)    # build a frequency map for numbers seen (one pass)
        unique_pairs = 0            # keep a counter for pairs seen

        # loop over frequency map, check if each key's complement is in the map, if it is add to counter
        for key in freq_map:
            if (k == 0 and freq_map[key] > 1) or (k > 0 and (key - k) in freq_map):
                unique_pairs += 1
        return unique_pairs
        # time complexity: O(n)
        # space complexity: O(n)
