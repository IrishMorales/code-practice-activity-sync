import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initial solution ---
        # sort the array, loop over nums every time a new element is encountered and k > 0, append new element to output then k -= 1
        # return output
        # time complexity: O(nlogn)
        # space complexity: O(n)

        # solution using hashmap ---
        # build a hashmap while going over array, keeping frequency of each element
        # return elements/keys with the highest values/counts
        freq_map = Counter(nums)
        sorted_freq = [k for k, v in sorted(freq_map.items(), reverse=True, key=lambda item: item[1])]
        return sorted_freq[:k]
        # time complexity: O(nlogn)
        # space complexity: O(n)
